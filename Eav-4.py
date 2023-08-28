def recommend_books(members, books):
    
    recommendations = {}
   
    for member in members:
        
        name = member["name"]
        genre = member["preferred_genre"]
        
        book = None
        
        for book in books:
            
            if book["genre"] == genre:
               
                book = book["title"]
              
                break
        
        recommendations[name] = book
   
    output = []
    
    for member, book in recommendations.items():
        
        recommendation = {"member": member, "book": book}
       
        output.append(recommendation)
    
    return output