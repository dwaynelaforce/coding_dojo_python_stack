from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
	if 'server_num' not in request.session:
		request.session['server_num'] = random.randint(1, 100)
	if 'user_guess_count' not in request.session:
		request.session['user_guess_count'] = 0
	print("server number is ", request.session['server_num'])
	print("user guesses so far: ", request.session['user_guess_count'])
	return render(request, 'index.html')

def user_guess(request):
	request.session['user_guess_count'] += 1
	guess = int(request.POST['user_number'])
	serverNum = request.session['server_num']
	if 'clue' not in request.session:
		request.session['clue'] = ""
	if guess > serverNum:
		clue = "Too high!"
	elif guess < serverNum:
		clue = "Too low!"
	else:
		clue = f"My number was {request.session['server_num']}.  You guessed it!"
		request.session['clue'] = clue
		return redirect('/correct')
	request.session['clue'] = clue
	return redirect('/')

def correct(request):
	return render(request, 'correct.html')


def play_again(request):
	request.session.flush()
	return redirect('/')
