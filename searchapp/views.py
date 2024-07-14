from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Dish
from .forms import SearchForm

def search(request):
    form = SearchForm()
    results = []
    if request.GET.get('query'):
        query = request.GET.get('query')
        results = Dish.objects.filter(name__icontains=query)
    return render(request, 'searchapp/search.html', {'form': form, 'results': results})



# def search(request):
#     form = SearchForm()
#     results = []
#     if request.GET.get('query'):
#         query = request.GET.get('query')

#         # Load data from CSV file
#         csv_path = os.path.join(os.path.dirname(__file__), 'data', 'restaurants_small.csv')
#         df = pd.read_csv(csv_path)

#         # Filter the dataframe for the query
#         filtered_df = df[df['name'].str.contains(query, case=False, na=False)]

#         # Convert the results to a list of dictionaries
#         results = filtered_df.to_dict('records')

#     return render(request, 'searchapp/search.html', {'form': form, 'results': results})
