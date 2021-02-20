import sys

def enter_list(x,number):
 m = 0
 for l in range(number):
     print('Enter the number of directions for the',l+1,'point')
     k = input()
     while True:
         if not k.isdigit() or int(k) > number:
             print("Pls enter the correct number! Try again: ")
             k = input()
         else:
             break
     k = int(k)
     if k == 0:
         continue
     print('Enter the', 1, 'direction for', l+1, 'point')
     b = input()
     while True:
         if not b.isdigit() or int(b) > number:
             print("Pls enter the correct number! Try again: ")
             b = input()
         else:
             break
     m += 1
     x[l][l - l] = int(b)
     for i in range(k-1):
         print('Enter the',i+2,'direction for',l+1,'point')
         p = input()
         m += 1
         while True:
             if not p.isdigit() or int(p) > number:
                 print("Pls enter the correct number! Try again: ")
                 p = input()
             else:
                 break
         x[l].append(int(p))
     x[l].append(int(0))
 return m
def enter_incidence_matrix(x):

    print("-" * (vertex + 13))
    for i in range(vertex):
        if i == 0 and vertex != 1:
            k = "Point    " + str(i + 1)
        else:
            if i == 0 and vertex == 1:
                k = "Point   " + str(i + 1) + "\n"
            else:
                if i + 1 == vertex:
                    k = " " + str(i + 1) + "\n"
                else:
                    k = " " + str(i + 1)
        sys.stdout.write(k)
    for i in range(directions):
        while True:
            try:
                    print("E(",i+1,") | ", end= '')
                    x[i] = [int(j) for j in input().strip().split(" ")]
                    if sum(x[i]) == 0 or (sum(x[i]) == 2 and x[i].count(0) == vertex - 1):
                        if (x[i].count(0) == vertex):
                            print("Vector is not singularity :) Repeat him")
                        else:
                            break
                    else:
                        print("You have something errors, check it and enter this line again")
            except:
                print("You have something errors, check it and enter this line again")
    print("-" * (vertex + 13))
    count = 0
    for i in range(directions):
        for l in range(directions-i):
            if x[i] == x[l] and i != l:
                print("Your matrix contains duplicate elements, re-enter it")
                enter_incidence_matrix(x)
    for i in range(directions):
        if vertex == 2:
            if x[i].count(0) == 2 or x[i].count(2) > 1 or sum(x[i]) > 2:
                print("You have something errors, check it and enter matrix again")
                enter_incidence_matrix(x)
            else:
                if x[i].count(-1) != x[i].count(1):
                    print("You have something errors, check it and enter matrix again")
                    enter_incidence_matrix(x)
        else:
            if x[i].count(0) == 1 and sum(x[i]) > 2 or x[i].count(0) > vertex - 2 and sum(x[i]) != 2:
                print("You have something errors, check it and enter matrix again")
                enter_incidence_matrix(x)
            else:
                if x[i].count(-1) != x[i].count(1):
                    print("You have something errors, check it and enter matrix again")
                    enter_incidence_matrix(x)
        for l in range(directions):
            if x[i] == x[l] and i != l:
                print("You have something errors, check it and enter matrix again")
                enter_incidence_matrix(x)
def enter_adjacency_matrix(x):
        print("-" * (vertex + 13))
        for i in range(vertex):
            if i == 0 and vertex != 1:
                k = "Point    " + str(i + 1)
            else:
                if i == 0 and vertex == 1:
                    k = "Point   " + str(i + 1) + "\n"
                else:
                    if i + 1 == vertex:
                        k = " " + str(i + 1) + "\n"
                    else:
                        k = " " + str(i + 1)
            sys.stdout.write(k)
        for i in range(vertex):
            while True:
                try:
                    print("X(", i + 1, ") | ", end='')
                    x[i] = [int(j) for j in input().strip().split(" ")]
                    if len(x[i]) > vertex or sum(x[i]) > vertex + 1 or x[i].count(2) > 1 or (x[i].count(2) == 1 and x[i].index(2) != i) or x[i].count(-1) == 1:
                        print("You have something errors, check it and enter this line again")
                    else:
                        break
                except:
                    print("You have something errors, check it and enter this line again")
        print("-" * (vertex + 13))
        if vertex == 2:
            if (x[0] != x[1]):
                print("You have something errors, check it and enter matrix again")
                enter_adjacency_matrix(x)
            else:
                if sum(x[0]) == 2 and sum(x[0]) == sum(x[1]):
                    print("You have something errors, check it and enter matrix again")
                    enter_adjacency_matrix(x)
        else:
            for i in range(vertex):
                if sum(x[i]) == 2 and x[i].count(2) == 1 and x[i][i] != 2:
                    print("You have something errors, check it and enter matrix again")
                    enter_adjacency_matrix(x)
def list_imatrix(x,y):
    i = 0
    j = 1
    u = 0
    while i < vertex:
         if int(len(x[i])) == 1:
            i += 1
         else:
            for l in range(int(len(x[i])) - 1):
                if i + 1 == x[i][l]:
                    y[u + j -1][i] = 2
                    u += 1
                else:
                        y[u + j - 1][i] = -1
                        y[u + j - 1][x[i][l] - 1] = 1
                        j += 1
            i += 1
            j -= 1
            u += 1
def list_amatrix(x,y):
    for i in range(vertex):
        if int(len(x[i])) != 1:
            for l in range(int(len(x[i])) - 1):
                if i + 1 == x[i][l]:
                    y[i][x[i][l]-1] = 2
                else:
                   y[i][x[i][l]-1] = 1
def imatrix_list(x,y):
    for i in range(directions):
        if x[i].count(0) != vertex:
            if x[i].count(-1) != 0:
                y[x[i].index(-1)].append(x[i].index(1)+1)
            else:
                y[x[i].index(2)].append(x[i].index(2) + 1)
    for i in range(vertex):
        if len(y[i]) >= 2 and y[i].count(0) == 1:
            del y[i][0]
            y[i].append(0)
def amatrix_list(x,y):
    size = 0
    for i in range(vertex):
        count = 0
        for l in range(vertex):
            if x[i][l] != 0:
                y[i].append(l+1)
                count += 1
                size += 1
            if count == (len(x[i])-x[i].count(0)):
                break
    for i in range(vertex):
        if len(y[i]) >= 2 and y[i].count(0) == 1:
            del y[i][0]
            y[i].append(0)
    return(size)

directions = 0
vertex = 0
imarray = []
amarray = []
larray = []
plot = 0
m=0
while True:
  if plot == 0:
    vertex = input("Enter the number of vertex: ")
    while True:
        if not vertex.isdigit():
            print("Pls enter the number without fractional part and positive! Try again: ")
            vertex = input()
        else:
            if int(vertex) == 0:
                print("Vertex zero? Seriosly? Man enter something more 0")
                vertex = input()
            else:
                break
    vertex = int(vertex)
    print("How do you want to enter the graph?")
    choose = input("````````````````````````````` \n"
                   "    1 -> ADJACENCY MATRIX     \n"
                   "````````````````````````````` \n"
                   "    2 -> INCIDENCE MATRIX     \n"
                   "````````````````````````````` \n"
                   "    3 ->  ADJACENCY LIST      \n"
                   "````````````````````````````` \n")
    while True:
        if not choose.isdigit() or int(choose) > 3 or int(choose) == 0 or int(choose) < 0:
            print("Ohh... PLS ENTER NUMBER 1, 2 OR 3! Try again: ")
            choose = input()
        else:
            break
    plot +=1
    choose = int(choose)
    if choose == 3:
        larray=[[0] for i in range(vertex)]
        m = enter_list(larray,vertex)
        imarray = [[0] * vertex for i in range(m)]
        list_imatrix(larray,imarray)
        amarray = [[0] * vertex for i in range(vertex)]
        list_amatrix(larray,amarray)
    if choose == 2:
        directions = input("Enter the amount of directions: ")
        while True:
            if not directions.isdigit():
                print(".... sh** enter the number without fraction part,maaaaan")
                directions = input()
            else:
                break
        directions = int(directions)
        directions2 = directions
        imarray = [[0] * vertex for i in range(directions)]
        print("E(i) - direction between 2 point \n"
              "if the point is the origin of this direction enter -1 \n"
              "if the point is the end of this direction enter 1 \n"
              "or if the point at the same time is the origin and the end enter 2 \n"
              "else enter 0")
        enter_incidence_matrix(imarray)
        larray = [[0] for i in range(vertex)]
        imatrix_list(imarray,larray)
        amarray = [[0] * vertex for i in range(vertex)]
        list_amatrix(larray, amarray)
    if choose == 1:
        amarray = [[0]* vertex for i in range(vertex)]
        print("Enter the matrix by this example: \n"
              "----------\n"
              "1 0 0 0 2 \n"
              "0 0 1 0 1 \n"
              "0 1 0 0 0 \n"
              "0 0 0 1 0 \n"
              "---------- ")
        enter_adjacency_matrix(amarray)
        larray = [[0] for i in range(vertex)]
        size_a = amatrix_list(amarray,larray)
        imarray = [[0] * vertex for i in range(size_a)]
        directions = size_a
        list_imatrix(larray,imarray)
  choose2 = input("Select an action: \n"
        "[ 1 ] - Show the incidence matrix\n"
        "[ 2 ] - Show the adjacency matrix\n"
        "[ 3 ] - Show the adjacency list\n"
        "[ 4 ] - Enter new data\n"
        "[ 5 ] - Exit the program: \n")
  while True:
      if not choose2.isdigit() or int(choose2) > 5 or int(choose2) == 0:
          print("Choose the correct item:")
          choose = input()
      else:
          break
  choose2 = int(choose2)
  if choose2 == 1:
      print("-" * (vertex + 15))
      print(" INCIDENCE MATRIX ")
      print("-" * (vertex + 15))
      for i in range(vertex):
          if i == 0 and vertex != 1:
              k = "Point     " + str(i + 1)
          else:
              if i == 0 and vertex == 1:
                  k = "Point    " + str(i + 1) + "\n"
              else:
                  if i + 1 == vertex:
                      k = " " + str(i + 1) + "\n"
                  else:
                      k = " " + str(i + 1)
          sys.stdout.write(k)
      if m != 0:
          directions = m
      for i in range(directions):
          if i+1 > 9:
              if imarray[i].count(-1) == 1:
                  print("E(",i+1,")|",*imarray[i],"|")
              else:
                  print("E(",i+1,")|",*imarray[i]," |")
          else:
              if imarray[i].count(-1) == 1:
                  print("E(",i+1,") |",*imarray[i],"|")
              else:
                  print("E(",i+1,") |",*imarray[i]," |")
      print("-"*(vertex+15))
  if choose2 == 2:
          print("-" * (vertex + 13))
          print(" ADJACENCY MATRIX ")
          print("-" * (vertex + 13))
          for i in range(vertex):
              if i == 0 and vertex != 1:
                  k = "Point   " + str(i + 1)
              else:
                  if i == 0 and vertex == 1:
                      k = "Point  " + str(i + 1) + "\n"
                  else:
                      if i + 1 == vertex:
                          k = " " + str(i + 1) + "\n"
                      else:
                          k = " " + str(i + 1)
              sys.stdout.write(k)
          for i in range(vertex):
              if i + 1 > 9:
                      print("X(",i + 1,") |", *amarray[i], "|")
              else:
                      print("X(",i + 1,")|", *amarray[i], "|")
          print("-" * (vertex + 13))
  if choose2 == 3:
      print("-"*(vertex+10))
      print(" ADJACENCY LIST ")
      print("-" * (vertex + 10))
      for i in range(vertex):
          print(i+1,"- ",end='')
          print(*larray[i], sep=', ')
      print("-" * (vertex + 10))
  if choose2 == 4:
      plot = 0
  if choose2 == 5:
      sys.exit()
