from django.shortcuts import render
from .forms import NumberPostForm, PostForm
import random
from .models import Item
  

def make_guess(request):
    guess = ''
    new_item = None
    if request.method == 'POST':
        form = NumberPostForm(data=request.POST)
        form_ans = PostForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            num_item = int(cd['num_item'])
            try:
                item = Item.objects.get(number=num_item)
                guess = item.color
                return render(request, 'home.html',
                    {'form': form, 
                    'guess': guess})
            except:
                pass
                
            blue = ['Синий'] * 50
            green = ['Зеленый'] * 30
            red = ['Красный'] * 20
            colors = red + green + blue
            ran_color = random.randint(0, len(colors)-1)
            guess = colors[ran_color]
        if form_ans.is_valid():
            new_item = form_ans.save()                            
    else:
        form = NumberPostForm()
        form_ans = PostForm()
    
    return render(request, 'home.html',
                  {'form': form,
                   'form_ans': form_ans, 
                   'guess': guess,
                   'new_item': new_item
                   })
    
  
