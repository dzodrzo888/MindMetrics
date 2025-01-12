from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import MoodTrackerForm
from .models import MoodTracker
from django.contrib import messages
from datetime import datetime
import pandas as pd
import seaborn as sns
import plotly.express as px


def home_view(request):
    context = {
        'is_logged_in': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else None
    }
    return render(request, 'index.html', context=context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
        elif None in [username, email, password]:
            messages.error(request, "Please fill in all required inputs!")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return render(request, 'index.html')

def quesstionaire_view(request):
    context = {
        'is_logged_in': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else None
    }
    return render(request, 'quesstionare.html', context=context)

@login_required
def quesstionaire_submit(request):
    if request.method == 'POST':
        form = MoodTrackerForm(request.POST)
        print("Post method good but form not valid")
        if form.is_valid():
            print("form valid")
            questionnaire = form.save(commit=False)
            questionnaire.user = request.user
            questionnaire.created_at = datetime.now()
            questionnaire.save()
            messages.success(request, "Questionnaire submitted successfully!")
            return redirect('quesstionaire')        
    return redirect('quesstionaire')  

def visulize_view(request):
    context = {
        'is_logged_in': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else None
    }
    return render(request, 'visualizer_home_page.html', context=context) 

@login_required
def data_processor(request):
    user_df_long = None
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        if start_date and end_date:
            mood_data = MoodTracker.objects.filter(user=request.user, created_at__range=[start_date, end_date])
        else:
            mood_data = MoodTracker.objects.filter(user=request.user)

        user_data = {
            "stress": [entry.stress for entry in mood_data],
            "anxiety": [entry.anxiety for entry in mood_data],
            "sleep": [entry.sleep for entry in mood_data],
            "mood": [entry.mood for entry in mood_data],
            "physical": [entry.physical for entry in mood_data],
            "water": [entry.water for entry in mood_data],
            "meal": [entry.meal for entry in mood_data],
            "nutrition": [entry.nutrition for entry in mood_data],
            "date": [entry.created_at for entry in mood_data],
        }
        user_df = pd.DataFrame(user_data)
            
        user_df_long = pd.melt(user_df, id_vars=["date"], 
                            var_name="Metrics", value_name="Score")
        messages.success(request, "Data returned")

    return user_df_long

@login_required
def data_visualizer(request):
    
    user_df_long = data_processor(request)

    if user_df_long is not None and not user_df_long.empty:

        fig = px.line(
            user_df_long,
            x="date",
            y="Score",
            color="Metrics",
            line_group="Metrics",
            markers=True,
            title="User Metrics Over Time",
            labels={"date": "Date", "Score": "Score", "Metrics": "Metrics"},
        )

        fig.update_layout(
            xaxis_title="date",
            yaxis_title="Score",
            legend_title="Metrics",
            template="plotly_white",
            xaxis=dict(tickmode="array", tickvals=user_df_long["date"].unique()),
        )

        plot_html = fig.to_html(full_html=False)

        context = {
            'is_logged_in': request.user.is_authenticated,
            'username': request.user.username if request.user.is_authenticated else None,
            'plot_html': plot_html,
        }

        return render(request, "interactive_plot.html", context=context)
    return redirect('data_visulize')