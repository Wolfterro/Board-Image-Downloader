#!/usr/bin/python2
# -*- coding: utf-8 -*-

'''
===========================

	Board Image Downloader

	Autor: Anonymous

	Modificação: Wolfterro
	Data: 10/04/2016
	Versão: 1.0

===========================
'''

from __future__ import print_function
import json
import urllib2
import os
import sys
import argparse

reload(sys)
sys.setdefaultencoding('utf-8')

DOWNLOAD_DIRECTORY = './Board_Image_Downloader'
BOARDS = []

def get_json(url):
	try:
		response = urllib2.urlopen(url)
		data = json.loads(response.read())
	except Exception as e:
		print('ERRO: Erro em get_json para %s\n  - %s' % (url, e))
		return {}
	return data

def print_progress(now, total, width=50):
	progress = float(now) / float(total)
	bar = ('#' * int(width * progress)).ljust(width)
	percent = progress * 100.0
	to_print = '[%s] %.2f%%\r' % (bar, percent)
	print(to_print, end='')
	if round(percent) >= 100:
		print('%s\r' % (' ' * len(to_print)), end='')

def download_with_progress(url, filename):
	response = urllib2.urlopen(url)
	total = response.headers['content-length']
	downloaded = 0
	with open(filename, 'wb') as file:
		while True:
			data = response.read(4096)
			downloaded += len(data)
			if not data:
				break
			file.write(data)
			print_progress(downloaded, total)

def get_boards():
	data = get_json('https://a.4cdn.org/boards.json')
	try:
		return [b['board'] for b in data['boards']]
	except:
		print('ERRO: Erro ao recuperar boards')
		return []

def get_posts(board, thread_no):
	data = get_json('https://a.4cdn.org/%s/thread/%s.json' % (board, thread_no))
	try:
		return data['posts']
	except:
		print('ERRO: Erro ao recuperar posts de tópico no. %d in /%s/' % (thread_no, board))
		return []

def get_images_from_posts(posts):
	return ['%s%s' % (p['tim'], p['ext']) for p in posts if 'tim' in p and 'ext' in p]

def download_image(board, image_name):
	url = 'http://i.4cdn.org/%s/%s' % (board, image_name)
	filename = os.path.join(DOWNLOAD_DIRECTORY, image_name)
	download_with_progress(url, filename)

def process_thread(board, thread_no):
	print('Fazendo download em /%s/ tópico no. %d' % (board, thread_no), end='')
	posts = get_posts(board, thread_no)
	images = get_images_from_posts(posts)
	print(' - Encontrada %d imagens em %d posts' % (len(images), len(posts)))
	downloaded = 0
	for image in images:
		os.chdir(DOWNLOAD_DIRECTORY)
		check_path_file = os.path.isfile(image)
		if check_path_file == True:
			downloaded += 1
			print('Imagem %s - imagem %d/%d em /%s/ tópico no. %d já existe! Pulando...' % (
				image, downloaded, len(images), board, thread_no))
		else:
			downloaded += 1
			print('Baixando %s - imagem %d/%d em /%s/ tópico no. %d' % (
				image, downloaded, len(images), board, thread_no))
			download_image(board, image)

def main():
	global DOWNLOAD_DIRECTORY, BOARDS

	parser = argparse.ArgumentParser(description='Board Image Downloader')
	parser.add_argument('-d', '--directory', help='Cria diretório para as imagens', default='')
	parser.add_argument('-b', '--boards', nargs='*', help='Seleciona imediatamente uma board', default=[])
	args = parser.parse_args()

	DOWNLOAD_DIRECTORY = args.directory or DOWNLOAD_DIRECTORY
	BOARDS = args.boards or BOARDS

	DOWNLOAD_DIRECTORY = os.path.expandvars(DOWNLOAD_DIRECTORY)
	DOWNLOAD_DIRECTORY = os.path.abspath(DOWNLOAD_DIRECTORY)
	print('Diretório de download é: %s' % DOWNLOAD_DIRECTORY)
	if not os.path.exists(DOWNLOAD_DIRECTORY):
		print('Diretório de download não existe! Criando...\n')
		os.makedirs(DOWNLOAD_DIRECTORY)

	if not BOARDS:
		print('Nenhuma board selecionada! Recuperando lista de todas as boards...\n')
		BOARDS = get_boards()
		print('Boards - /%s/' % ('/, /'.join(BOARDS)))
		print('')
		board = raw_input("Insira a board desejada sem as barras (exemplo: gif): ")
	else:
		for board_list in BOARDS:
			board = board_list

	thread_number = int(raw_input("Insira o número do tópico desejado (exemplo: 8364104): "))
	print('')
	
	process_thread(board, thread_number)

if __name__ == '__main__':
	main()