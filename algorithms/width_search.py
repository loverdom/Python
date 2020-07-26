from collections import deque
  

def person_is_seller(name):
    if name[-1] == 'y':
        return True
    else:
        return False

def search(name):
    search = deque()
    search += graph[name]
    searched = []
    while search:
        person = search.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is mango seller")
                print(search)
                return True
            else:
                print(search)
                search += graph[person]
                searched.append(person)
    return False

graph = {}
graph["You"] = ["Alice", "Claire", "Bob"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["Tom", "John"]
graph["Bob"] = ["Anuj", "Peggy"]


search("You")    
