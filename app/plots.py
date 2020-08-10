# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 10:57:57 2020

@author: rober
"""

import plotly
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np



def create_plot(df):

    df['sim_index'] = np.round(df['sim_index'],4) 
    df['p_def'] = np.round(df['p_def'],4) 

    for col in df.columns:
        df[col] = df[col].astype(str)
    
    scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(0,191,255)'],[0.4, 'rgb(30,144,255)'],\
                    [0.6, 'rgb(0,0,255)'],[0.8, 'rgb(0,0,205)'],[1.0, 'rgb(0,0,139)']] 
    
    df['text'] = df['Code'] + '<br>' + 'def. prob. ' + df['p_def']
    
    data = [ dict(
            type='choropleth',
            colorscale = scl,
            autocolorscale = False,
            locations = df['Code'],
            z = df['sim_index'], 
            locationmode = 'USA-states',
            text = df['text'],
            marker = dict(
                line = dict (
                    #color = 'rgb(0,0,0)',
                    color = 'black',
                    width = 1.5
                ) ),
            colorbar = dict(
                title = "Similarity<br>Index")
            ) ]    
    
    layout = dict(
        title = 'By State Model Results<br>and Similarity<br>(Hover for detail)',
        geo = dict(
            scope = 'usa',
            projection=dict(type='albers usa'),
            showlakes = False,
            lakecolor = 'rgb(255, 255, 255)')            
    )
    
    fig = dict( data=data, layout=layout )
    fig_div = plotly.offline.plot(
            fig,
            image_width='100%',
            image_height='100%',
            include_plotlyjs=False,
            output_type='div',
            auto_open=False,
            )
   
    return fig_div



def calculate_rings(p):
    p = round(p, 2)
    b = 100
    a = p * 100    
    rings=[[a,b-a],[0,0]]  
    return rings


    
def add_center_label(p):    
    percent = str(round(p*100,2)) + '%'
    return plt.text(0,
           0,
           percent,
           horizontalalignment='center',
           verticalalignment='center',
           fontsize = 40,
           family = 'sans-serif')
    

def plot2(p):    
    # base styling logic
    color_theme = 'Blue'
    color = plt.get_cmap(color_theme + 's')
    ring_width = 0.3
    outer_radius = 1.5
    inner_radius = outer_radius - ring_width   

    # set up plot
    ring_arrays = calculate_rings(p)
    fig, ax = plt.subplots()
    
    outer_edge_color, inner_edge_color = ['white', None]

    # plot logic
    outer_ring, _ = ax.pie(ring_arrays[0],radius=1.5,
                colors=[color_theme, color(0.11)],
                startangle = 90,
                counterclock = False)
    
    plt.setp( outer_ring, width=ring_width, edgecolor=outer_edge_color)

    inner_ring, _ = ax.pie(ring_arrays[1],
                     radius=inner_radius,
                     colors=[color(0.55), color(0.05)],
                     startangle = 90,
                     counterclock = False)
    
    plt.setp(inner_ring, width=ring_width, edgecolor=inner_edge_color)

    # add labels and format plots
    add_center_label(p)  
    ax.axis('equal')
    plt.margins(0,0)
    plt.autoscale('enable')       
    
    
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    return pngImageB64String


