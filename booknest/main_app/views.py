from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Author:
    def __init__(self, name, age, genre, nationality, bio):
        self.name = name
        self.age = age
        self.genre = genre
        self.nationality = nationality
        self.bio = bio

authors = [
    Author('John Saul', '82', 'Suspense & Horror', 'American', "John Saul (1942-2023) was an American author known for his psychological and supernatural horror novels. He published over 30 books, many of which became bestsellers, including Suffer the Children (1977), Creature (1989), and The Blackstone Chronicles (1997). His works often feature small-town settings, dark secrets, and characters facing eerie and terrifying events. Saul's storytelling blended suspense, horror, and psychological depth, earning him a dedicated fanbase."),
    Author('Stephenie Meyer', '51', 'Sci-Fi', 'American', "Stephenie Meyer (born 1973) is an American author best known for her Twilight saga, a bestselling vampire romance series that gained worldwide popularity. The series, which includes Twilight (2005), New Moon (2006), Eclipse (2007), and Breaking Dawn (2008), has sold over 160 million copies and was adapted into a successful film franchise. Meyer also wrote The Host (2008), a sci-fi novel, and Midnight Sun (2020), a retelling of Twilight from Edward Cullen’s perspective. Her work is credited with revitalizing the young adult paranormal romance genre."),
    Author('J.K. Rowling', '59', 'Fantasy', 'British', "J.K. Rowling (born 1965) is a British author best known for creating the Harry Potter series, one of the best-selling book franchises in history. The series, which includes seven books published between 1997 and 2007, follows the journey of a young wizard, Harry Potter, and his battle against the dark wizard Lord Voldemort. The books have sold over 500 million copies worldwide and were adapted into a blockbuster film series. Rowling has also written crime fiction under the pseudonym Robert Galbraith, including the Cormoran Strike series. In addition to her literary success, she is known for her philanthropy and involvement in social issues.")
]

def author_index(request):
    return render(request, 'authors/index.html', {'authors': authors})
