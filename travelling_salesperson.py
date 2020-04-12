#!/usr/bin/env python
# coding: utf-8

# In[700]:


import csv
#import pandas
from random import shuffle, randint
from math import sin, cos, sqrt, atan2, radians, factorial


# In[657]:


def transpose(A):
    return list(map(list,zip(*A)))


# In[664]:


class graph:
    def __init__(self, nodes=['United Kingdom','France','Germany','Italy','Spain','Egypt']):
        self.nodes = nodes
        self.roadmap = self.roadmap(self.nodes)
        self.num_nodes = len(self.nodes)
        self.min = nodes
        self.min_dis = distance(points=self.roadmap)
    def roadmap(self,nodes):
        loc = []
        with open('cities.csv') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                if row[3] in nodes:
                    loc.append([row[3],[float(row[1]),float(row[2])]])
        #print(loc)
        return loc

    def distance(self,points=False,total=True):
        dis_tot = 0
        dis_list = []
        if points == False:
            points = self.roadmap
        # approximate radius of earth in km
        R = 6373.0
        nxt_points = points[1:] + points[0:]
        for p1,p2 in zip(points,nxt_points):
            lat1 = radians(p1[1][0])
            lon1 = radians(p1[1][1])
            lat2 = radians(p2[1][0])
            lon2 = radians(p2[1][1])

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = R * c
            if total:
                dis_tot += distance
            else:
                dis_list.append([f'{p1[0]} -> {p2[0]}',distance])
        if total:
            return dis_tot
        else:
            return dis_list
    def new_cyc(self):
        nodes = self.roadmap
        pem = list(range(1,len(nodes)))
        shuffle(pem)
        new_path = [nodes[0]]
        for j in pem:
            #print(nodes[i],j)
            new_path.append(nodes[j])
        return new_path
    def minimise(self): 
        thresh = self.min_dis
        dis = thresh + 1
        #max_count = int(factorial(self.num_nodes-1)*0.80)
        count = 1        
        ###Stop Conditions
        ##Stop if count is greater than maximum
        #(count < max_count) and (dis > thresh)
        ##Stop if more than 3 repeats
        #count > 3
        
        while (count < 5):
            new = self.new_cyc()
           #print(len(new))
            dis = self.distance(new)
            if dis < thresh:
                mini = transpose(new)[0]
                thresh = dis
            elif dis == thresh:
                count += 1
                
            #print(f'Threshold: {thresh}\n current: {dis}\n {count}')
            
        if dis < self.min_dis:
            self.min = mini
            self.min_dis = thresh
            print(f'New min found\n path: {self.min}\n distance: {dis:.0f} km')
        else:
            print(f'Shorter path not found\n min path still: {self.min}\n distance: {self.min_dis:.0f} km')


# In[699]:


def main():
    
    g = graph()
    print(f'Initial path: {g.nodes}')
    g.minimise()
if __name__ == '__main__':
    main()

