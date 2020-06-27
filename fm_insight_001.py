#!/usr/bin/env python
# coding: utf-8

# In[81]:


# Import required packages
import pandas as pd
import plotly.express as px
import plotly.io as pio
from easygui import *
import numpy as np
import os
#import matplotlib.pyplot as plt
#import seaborn as sns
pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows',100)
pd.set_option('precision', 0)


# In[82]:


# Choose between own squad or scouting results
choice = buttonbox ("Please choose data source:", 
                    title = "Data source selection", choices = ["Own Squad", "Scouting Results"])
if choice == "Own Squad":
    df = pd.read_html(r"C:\\Users\\stuar\\Documents\\Sports Interactive\\Football Manager 2020\\html\\squad_python.html",skiprows=0,)[0]    
elif choice == "Scouting Results":
    df = pd.read_html(r"C:\\Users\\stuar\\Documents\\Sports Interactive\\Football Manager 2020\\html\\scouting_python.html",skiprows=0,)[0]


# In[83]:


# Convert wages and player value to float minus characters
for column in ['Value', 'Wage','Dist/90'
              ]:
    df[column] = df[column].str.replace('-','0')
    df[column] = df[column].str.replace('£','')
    df[column] = df[column].str.replace('Â','')
    df[column] = df[column].str.replace('p/w','')
    df[column] = df[column].str.replace(',','')
    df[column] = df[column].str.replace('K','000')
    df[column] = df[column].str.replace('.','')
    df[column] = df[column].str.replace('km','')
    df[column] = df[column].str.replace('M','00000').astype(float)


# In[84]:


for column in ['Svt', 'Svh', 'Svp', 'Ch C/90', 'DrbPG', 'Cr C', 'Tck R', 'Int/90', 'K Ps/90', 'Hdrs W/90', 
                   'Hdr %', 'Ps C/90', 'Pas %', 'Gls/90', 'Asts/90', 'ShT/90', 'Tcon/90', 'Shot %', 'Cr C/A', 'Ps A/90',
                   'Tcon', 'Conc', 'Gls', 'Mins', 'Av Rat', 'Ast', 'Tck.1',
              ]:                  
    df[column] = df[column].str.replace('-','0')
    df[column] = df[column].str.replace('%','').astype(float)


# In[85]:


#df.info()


# In[86]:


# Create Saves_90 metric (saves made per 90)
df['Tot_Sav'] = df['Svp'] + df['Svh'] + df['Svt']
df['Per_90'] = df['Mins'] / 90
df['Saves_90'] = df['Tot_Sav'] / df['Per_90']

#Create Faced_90 metric (shots faced per 90)
df['Shots_Faced'] = df['Conc'] + df['Tot_Sav']
df['Faced_90'] = df['Shots_Faced'] / df['Per_90']

# Create score for each position and club DNA.\n",
df['dna'] = df['Agg'] + df['Ant'] + df['Det'] + df['Tea'] + df['Wor'] + df['Acc'] + df['Sta']
df['sk_su'] = df['Aer'] + df['Cmd'] + df['Com'] + df['Han'] + df['Kic'] + df['Ref'] + df['TRO'] + df['Thr'] + df['1v1'] + df['Pas'] + df['Fir'] + df['Ant'] + df['Vis'] + df['Dec'] + df['Pos'] + df['Cmp'] + df['Cnt'] + df['Acc'] + df['Agi']
df['cd_de'] = df['Hea'] + df['Mar'] + df['Tck'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Dec'] + df['Pos'] + df['Cmp'] + df['Cnt'] + df['Pac'] + df['Str'] + df['Jum'] 
df['wb_su'] = df['Cro'] + df['Dri'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Tec'] + df['Fir'] + df['Ant'] + df['Dec'] + df['OtB'] + df['Pos'] + df['Tea'] + df['Wor'] + df['Cnt'] + df['Acc'] + df['Agi'] + df['Pac'] + df['Sta']
df['wb_at'] = df['Cro'] + df['Dri'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Tec'] + df['Fir'] + df['Ant'] + df['Dec'] + df['Fla'] + df['OtB'] + df['Pos'] + df['Tea'] + df['Wor'] + df['Cnt'] + df['Acc'] + df['Agi'] + df['Pac']+ df['Sta'] 
df['cwb_su'] = df['Cro'] + df['Dri'] + df['Pas'] + df['Tck'] + df['Tec'] + df['Fir'] + df['Ant'] + df['Dec'] + df['Fla'] + df['OtB'] + df['Tea'] + df['Wor'] + df['Cmp'] + df['Acc'] + df['Agi'] + df['Bal'] + df['Pac'] + df['Sta']
df['dm_de'] = df['Mar'] + df['Pas'] + df['Tck'] + df['Agg'] + df['Ant'] + df['Dec'] + df['Pos'] + df['Tea'] + df['Wor'] + df['Cmp'] + df['Cnt'] + df['Sta'] + df['Str'] 
df['bwm_su'] = df['Mar'] + df['Pas'] + df['Tck'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Tea'] + df['Wor'] + df['Cnt'] + df['Agi'] + df['Pac'] + df['Sta'] + df['Str'] 
df['dlp_su'] = df['Pas']  + df['Tec']  + df['Fir']  + df['Ant']  + df['Vis']  + df['Dec']  + df['OtB']  + df['Tea']  + df['Wor']  + df['Cmp']  + df['Bal'] 
df['vol_su'] = df['Fin'] + df['Lon'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Fir'] + df['Ant'] + df['Dec'] + df['OtB'] + df['Pos'] + df['Wor'] + df['Cmp'] + df['Cnt'] + df['Acc'] + df['Bal'] + df['Pac'] + df['Sta'] + df['Str']
df['car_su'] = df['Pas'] + df['Tck'] + df['Tec'] + df['Fir'] + df['Ant'] + df['Vis'] + df['Dec'] + df['OtB'] + df['Pos'] + df['Tea'] + df['Wor'] + df['Cmp'] + df['Cnt'] + df['Sta'] 
df['iw_at'] = df['Cro'] + df['Dri'] + df['Lon'] + df['Pas'] + df['Tec'] + df['Fir'] + df['Ant'] + df['Vis'] + df['Dec'] + df['Fla'] + df['OtB'] + df['Cmp'] + df['Acc'] + df['Agi'] + df['Pac'] 
df['if_su'] = df['Dri'] + df['Fin'] + df['Lon'] + df['Pas'] + df['Tec'] + df['Fir'] + df['Ant'] + df['Vis'] + df['Fla'] + df['OtB'] + df['Cmp'] + df['Acc'] + df['Agi'] + df['Bal'] + df['Pac']
df['if_at'] = df['Dri'] + df['Fin'] + df['Lon'] + df['Pas'] + df['Tec'] + df['Fir'] + df['Ant'] + df['Fla'] + df['OtB'] + df['Cmp'] + df['Acc'] + df['Agi'] + df['Bal'] + df['Pac']
df['am_su'] = df['Dri']  + df['Lon']  + df['Pas']  + df['Tec']  + df['Fir']  + df['Ant']  + df['Vis']  + df['Dec']  + df['Fla']  + df['OtB']  + df['Cmp']  + df['Agi']
df['ap_su'] = df['Dri']  + df['Pas']  + df['Tec']  + df['Fir']  + df['Ant']  + df['Vis']  + df['Dec']  + df['Fla']  + df['OtB']  + df['Tea']  + df['Cmp']  + df['Agi']
df['f9_su'] = df['Dri'] + df['Fin'] + df['Pas'] + df['Tec'] + df['Fir'] + df['Ant'] + df['Vis'] + df['Dec'] + df['Fla'] + df['OtB'] + df['Tea'] + df['Cmp'] + df['Acc'] + df['Agi'] + df['Bal'] 
df['pf_at'] = df['Fin'] + df['Fir'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Dec'] + df['OtB'] + df['Tea'] + df['Wor'] + df['Cmp'] + df['Cnt'] + df['Acc'] + df['Agi'] + df['Bal'] + df['Pac'] + df['Sta'] + df['Str']
 
# Create custom DataFrame for each position and club DNA
dna = df[['Name', 'Personality', 'Age', 'Agg','Ant','Det','Tea','Wor','Acc','Sta','dna']]
sk_su = df[['Name', 'Age', 'Aer', 'Cmd', 'Com', 'Han', 'Kic', 'Ref', 'TRO', 'Thr', '1v1', 'Pas', 'Fir', 'Ant', 'Vis', 'Dec', 'Pos', 'Cmp', 'Cnt', 'Acc', 'Agi', 'sk_su']] 
cd_de = df[['Name', 'Age', 'Hea', 'Mar', 'Tck', 'Agg', 'Ant', 'Bra', 'Dec', 'Pos', 'Cmp', 'Cnt', 'Pac', 'Str', 'Jum', 'cd_de']] 
wb_su = df[['Name', 'Age', 'Cro', 'Dri', 'Mar', 'Pas', 'Tck', 'Tec', 'Fir', 'Ant', 'Dec', 'OtB', 'Pos', 'Tea', 'Wor', 'Cnt', 'Acc', 'Agi', 'Pac', 'Sta', 'wb_su']]
wb_at = df[['Name', 'Age', 'Cro', 'Dri', 'Mar', 'Pas', 'Tck', 'Tec', 'Fir', 'Ant', 'Dec', 'Fla', 'OtB', 'Pos', 'Tea', 'Wor', 'Cnt', 'Acc', 'Agi', 'Pac', 'Sta', 'wb_at']] 
cwb_su = df[['Name', 'Age', 'Cro', 'Dri', 'Pas', 'Tck', 'Tec', 'Fir', 'Ant', 'Dec', 'Fla', 'OtB', 'Tea', 'Wor', 'Cmp', 'Acc', 'Agi', 'Bal', 'Pac', 'Sta', 'cwb_su']]
dm_de = df[['Name', 'Age', 'Mar', 'Pas', 'Tck', 'Agg', 'Ant', 'Dec', 'Pos', 'Tea', 'Wor', 'Cmp', 'Cnt', 'Sta', 'Str', 'dm_de']]
bwm_su = df[['Name', 'Age', 'Mar', 'Pas', 'Tck', 'Agg', 'Ant', 'Bra', 'Tea', 'Wor', 'Cnt', 'Agi', 'Pac', 'Sta', 'Str', 'bwm_su']]
dlp_su = df[['Name', 'Age', 'Pas', 'Tec', 'Fir', 'Ant', 'Vis', 'Dec', 'OtB', 'Tea', 'Wor', 'Cmp', 'Bal', 'dlp_su']]
vol_su = df[['Name', 'Age', 'Fin' , 'Lon' , 'Mar' , 'Pas' , 'Tck' , 'Fir' , 'Ant' , 'Dec' , 'OtB' , 'Pos' , 'Wor' , 'Cmp' , 'Cnt' , 'Acc' , 'Bal' , 'Pac' , 'Sta' , 'Str', 'vol_su']]
car_su = df[['Name', 'Age', 'Pas' , 'Tck' , 'Tec' , 'Fir' , 'Ant' , 'Vis' , 'Dec' , 'OtB' , 'Pos' , 'Tea' , 'Wor' , 'Cmp' , 'Cnt' , 'Sta', 'car_su']]
iw_at = df[['Name', 'Age', 'Cro' , 'Dri' , 'Lon' , 'Pas' , 'Tec' , 'Fir' , 'Ant' , 'Vis' , 'Dec' , 'Fla' , 'OtB' , 'Cmp' , 'Acc' , 'Agi' , 'Pac', 'iw_at']] 
if_su = df[['Name', 'Age', 'Dri' , 'Fin' , 'Lon' , 'Pas' , 'Tec' , 'Fir' , 'Ant' , 'Vis' , 'Fla' , 'OtB' , 'Cmp' , 'Acc' , 'Agi' , 'Bal' , 'Pac', 'if_su']]
if_at = df[['Name', 'Age', 'Dri' , 'Fin' , 'Lon' , 'Pas' , 'Tec' , 'Fir' , 'Ant' , 'Fla' , 'OtB' , 'Cmp' , 'Acc' , 'Agi' , 'Bal' , 'Pac', 'if_at']]
am_su = df[['Name', 'Age', 'Dri', 'Lon', 'Pas', 'Tec', 'Fir', 'Ant', 'Vis', 'Dec', 'Fla', 'OtB', 'Cmp', 'Agi', 'am_su']]
ap_su = df[['Name', 'Age', 'Dri', 'Pas', 'Tec', 'Fir', 'Ant', 'Vis', 'Dec', 'Fla', 'OtB', 'Tea', 'Cmp', 'Agi', 'ap_su']]
f9_su = df[['Name', 'Age', 'Dri' , 'Fin' , 'Pas' , 'Tec' , 'Fir' , 'Ant' , 'Vis' , 'Dec' , 'Fla' , 'OtB' , 'Tea' , 'Cmp' , 'Acc' , 'Agi' , 'Bal', 'f9_su']]
pf_at = df[['Name', 'Age', 'Fin' , 'Fir' , 'Agg' , 'Ant' , 'Bra' , 'Dec' , 'OtB' , 'Tea' , 'Wor' , 'Cmp' , 'Cnt' , 'Acc' , 'Agi' , 'Bal' , 'Pac' , 'Sta' , 'Str', 'pf_at']]

choice = buttonbox ("What would you like to analyse?", 
                    title = "Data source selection", choices = ["dna", "sk_su",
                    "cd_de", "wb_su", "wb_at", "cwb_su", "dm_de", "bwm_su", "dlp_su",
                    "vol_su", "car_su", "iw_at","if_su", "if_at", "am_su", "ap_su",
                    "f9_su", "pf_at", "squad"])
if choice == "dna":
    sortchoice = dna
    tablechoice = 'dna'
elif choice == "sk_su":
    sortchoice = sk_su
    tablechoice = 'sk_su'
    fig = px.scatter(df, x="Faced_90", y="Saves_90", text="Name", log_x=False, size_max=60)
    fig.update_traces(textposition='top center')
    fig.update_layout(height=500)
    fig.update_xaxes(title_text='Shots faced/90')
    fig.update_yaxes(title_text='Saves made/90')
    fig.update_layout(template="plotly_dark",title="Shot Stopping")
    fig.show()
elif choice == "cd_de":
    sortchoice = cd_de
    tablechoice = 'cd_de'
    fig1 = px.scatter(df, x="Tck", y="Int/90", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Tackles Won/90')
    fig1.update_yaxes(title_text='Interceptions/90')
    fig1.update_layout(template="plotly_dark",title="Ground Duels")
    fig1.show()
    fig2 = px.scatter(df, x="Hdrs W/90", y="Hdr %", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Headers Won/90')
    fig2.update_yaxes(title_text='Headers Won %')
    fig2.update_layout(template="plotly_dark",title="Aerial Duels")
    fig2.show()
elif choice == "wb_su":
    sortchoice = wb_su
    tablechoice = 'wb_su'
    fig1 = px.scatter(df, x="Tck", y="Int/90", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Tackles Won/90')
    fig1.update_yaxes(title_text='Interceptions/90')
    fig1.update_layout(template="plotly_dark",title="Ground Duels")
    fig1.show()
    fig2 = px.scatter(df, x="Ch C/90", y="DrbPG", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Progressive Passes/90')
    fig2.update_yaxes(title_text='Progressive Runs/90')
    fig2.update_layout(template="plotly_dark",title="Ball carrying skills")
    fig2.show()
    fig3 = px.scatter(df, x="Cr C", y="Cr C/A", text="Name", log_x=False, size_max=60)
    fig3.update_traces(textposition='top center')
    fig3.update_layout(height=500)
    fig3.update_xaxes(title_text='Crossed Completed/90')
    fig3.update_yaxes(title_text='Crossing Accuracy')
    fig3.update_layout(title="Crossing ability")
    fig3.show()
elif choice == "wb_at":
    sortchoice = wb_at
    tablechoice = 'wb_at'
    fig1 = px.scatter(df, x="Tck", y="Int/90", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Tackles Won/90')
    fig1.update_yaxes(title_text='Interceptions/90')
    fig1.update_layout(template="plotly_dark",title="Ground Duels")
    fig1.show()
    fig2 = px.scatter(df, x="Ch C/90", y="DrbPG", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Progressive Passes/90')
    fig2.update_yaxes(title_text='Progressive Runs/90')
    fig2.update_layout(template="plotly_dark",title="Ball carrying skills")
    fig2.show()
    fig3 = px.scatter(df, x="Cr C", y="Cr C/A", text="Name", log_x=False, size_max=60)
    fig3.update_traces(textposition='top center')
    fig3.update_layout(height=500)
    fig3.update_xaxes(title_text='Crossed Completed/90')
    fig3.update_yaxes(title_text='Crossing Accuracy')
    fig3.update_layout(template="plotly_dark",title="Crossing ability")
    fig3.show()
elif choice == "cwb_su":
    sortchoice = cwb_su
    tablechoice = 'cwb_su'
    fig1 = px.scatter(df, x="Tck", y="Int/90", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Tackles Won/90')
    fig1.update_yaxes(title_text='Interceptions/90')
    fig1.update_layout(template="plotly_dark",title="Ground Duels")
    fig1.show()
    fig2 = px.scatter(df, x="Ch C/90", y="DrbPG", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Progressive Passes/90')
    fig2.update_yaxes(title_text='Progressive Runs/90')
    fig2.update_layout(template="plotly_dark",title="Ball carrying skills")
    fig2.show()
    fig3 = px.scatter(df, x="Cr C", y="Cr C/A", text="Name", log_x=False, size_max=60)
    fig3.update_traces(textposition='top center')
    fig3.update_layout(height=500)
    fig3.update_xaxes(title_text='Crossed Completed/90')
    fig3.update_yaxes(title_text='Crossing Accuracy')
    fig3.update_layout(template="plotly_dark",title="Crossing ability")
    fig3.show()
elif choice == "dm_de":
    sortchoice = dm_de
    tablechoice = 'dm_de'
    fig1 = px.scatter(df, x="Tck", y="Int/90", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Tackles Won/90')
    fig1.update_yaxes(title_text='Interceptions/90')
    fig1.update_layout(template="plotly_dark",title="Ground Duels")
    fig1.show()
    fig2 = px.scatter(df, x="Ps C/90", y="Pas %", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Passes Completed/90')
    fig2.update_yaxes(title_text='Pass Completion %')
    fig2.update_layout(template="plotly_dark",title="Passing Ability")
    fig2.show()
elif choice == "bwm_su":
    sortchoice = bwm_su
    tablechoice = 'bwm_su'
    fig1 = px.scatter(df, x="Tck", y="Int/90", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Tackles Won/90')
    fig1.update_yaxes(title_text='Interceptions/90')
    fig1.update_layout(template="plotly_dark",title="Ground Duels")
    fig1.show()
    fig2 = px.scatter(df, x="Ps C/90", y="Pas %", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Passes Completed/90')
    fig2.update_yaxes(title_text='Pass Completion %')
    fig2.update_layout(template="plotly_dark",title="Passing Ability")
    fig2.show()
elif choice == "dlp_su":
    sortchoice = dlp_su
    tablechoice = 'dlp_su'
    fig1 = px.scatter(df, x="Tck", y="Int/90", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Tackles Won/90')
    fig1.update_yaxes(title_text='Interceptions/90')
    fig1.update_layout(template="plotly_dark",title="Ground Duels")
    fig1.show()
    fig2 = px.scatter(df, x="Ps C/90", y="Pas %", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Passes Completed/90')
    fig2.update_yaxes(title_text='Pass Completion %')
    fig2.update_layout(template="plotly_dark",title="Passing Ability")
    fig2.show()
elif choice == "vol_su":
    sortchoice = vol_su
    tablechoice = 'vol_su'
    fig1 = px.scatter(df, x="Ps C/90", y="Pas %", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Passes Completed/90')
    fig1.update_yaxes(title_text='Pass Completion %')
    fig1.update_layout(template="plotly_dark",title="Passing Ability")
    fig1.show()
    fig2 = px.scatter(df, x="Ch C/90", y="DrbPG", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Progressive Passes/90')
    fig2.update_yaxes(title_text='Progressive Runs/90')
    fig2.update_layout(template="plotly_dark",title="Ball carrying skills")
    fig2.show()
elif choice == "car_su":
    sortchoice = car_su
    tablechoice = 'car_su'
    fig1 = px.scatter(df, x="Ps C/90", y="Pas %", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Passes Completed/90')
    fig1.update_yaxes(title_text='Pass Completion %')
    fig1.update_layout(template="plotly_dark",title="Passing Ability")
    fig1.show()
    fig2 = px.scatter(df, x="Ch C/90", y="DrbPG", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Progressive Passes/90')
    fig2.update_yaxes(title_text='Progressive Runs/90')
    fig2.update_layout(template="plotly_dark",title="Ball carrying skills")
    fig2.show()
elif choice == "iw_at":
    sortchoice = iw_at
    tablechoice = 'iw_at'
    fig1 = px.scatter(df, x="Ch C/90", y="DrbPG", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Progressive Passes/90')
    fig1.update_yaxes(title_text='Progressive Runs/90')
    fig1.update_layout(template="plotly_dark",title="Ball carrying skills")
    fig1.show()
    fig2 = px.scatter(df, x="Cr C", y="K Ps/90", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Crossed Completed/90')
    fig2.update_yaxes(title_text='Key Passes/90')
    fig2.update_layout(template="plotly_dark",title="Wide Creation")
    fig2.show()
elif choice == "if_su":
    sortchoice = if_su
    tablechoice = 'if_su'
    fig1 = px.scatter(df, x="Ch C/90", y="DrbPG", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Progressive Passes/90')
    fig1.update_yaxes(title_text='Progressive Runs/90')
    fig1.update_layout(template="plotly_dark",title="Ball carrying skills")
    fig1.show()
    fig2 = px.scatter(df, x="Cr C", y="K Ps/90", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Crossed Completed/90')
    fig2.update_yaxes(title_text='Key Passes/90')
    fig2.update_layout(template="plotly_dark",title="Wide Creation")
    fig2.show()
elif choice == "if_at":
    sortchoice = if_at
    tablechoice = 'if_at'
    fig1 = px.scatter(df, x="Ch C/90", y="DrbPG", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Progressive Passes/90')
    fig1.update_yaxes(title_text='Progressive Runs/90')
    fig1.update_layout(template="plotly_dark",title="Ball carrying skills")
    fig1.show()
    fig2 = px.scatter(df, x="Gls/90", y="ShT/90", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Goals/90')
    fig2.update_yaxes(title_text='Shots on Target/90')
    fig2.update_layout(template="plotly_dark",title="Goalscoring Efficiency")
    fig2.show()
elif choice == "am_su":
    sortchoice = am_su
    tablechoice = 'am_su'
    fig1 = px.scatter(df, x="Ch C/90", y="DrbPG", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Progressive Passes/90')
    fig1.update_yaxes(title_text='Progressive Runs/90')
    fig1.update_layout(template="plotly_dark",title="Ball carrying skills")
    fig1.show()
    fig2 = px.scatter(df, x="Ps C/90", y="Pas %", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Passes Completed/90')
    fig2.update_yaxes(title_text='Pass Completion %')
    fig2.update_layout(template="plotly_dark",title="Passing Ability")
    fig2.show()
    fig3 = px.scatter(df, x="Gls/90", y="Asts/90", text="Name", log_x=False, size_max=60)
    fig3.update_traces(textposition='top center')
    fig3.update_layout(height=500)
    fig3.update_xaxes(title_text='Goals/90')
    fig3.update_yaxes(title_text='Assists/90')
    fig3.update_layout(template="plotly_dark",title="Attacking Impact")
    fig3.show()
elif choice == "ap_su":
    sortchoice = ap_su
    tablechoice = 'ap_su'
    fig1 = px.scatter(df, x="Ch C/90", y="DrbPG", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Progressive Passes/90')
    fig1.update_yaxes(title_text='Progressive Runs/90')
    fig1.update_layout(template="plotly_dark",title="Ball carrying skills")
    fig1.show()
    fig2 = px.scatter(df, x="Ps C/90", y="Pas %", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Passes Completed/90')
    fig2.update_yaxes(title_text='Pass Completion %')
    fig2.update_layout(template="plotly_dark",title="Passing Ability")
    fig2.show()
    fig3 = px.scatter(df, x="Gls/90", y="Asts/90", text="Name", log_x=False, size_max=60)
    fig3.update_traces(textposition='top center')
    fig3.update_layout(height=500)
    fig3.update_xaxes(title_text='Goals/90')
    fig3.update_yaxes(title_text='Assists/90')
    fig3.update_layout(title="Attacking Impact")
    fig3.show()
elif choice == "f9_su":
    sortchoice = f9_su
    tablechoice = 'f9_su'
    fig1 = px.scatter(df, x="Gls/90", y="Asts/90", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Goals/90')
    fig1.update_yaxes(title_text='Assists/90')
    fig1.update_layout(template="plotly_dark",title="Attacking Impact")
    fig1.show()
    fig2 = px.scatter(df, x="Gls/90", y="ShT/90", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Goals/90')
    fig2.update_yaxes(title_text='Shots on Target/90')
    fig2.update_layout(template="plotly_dark",title="Goalscoring Efficiency")
    fig2.show()
elif choice == "pf_at":
    sortchoice = pf_at
    tablechoice = 'pf_at'
    fig1 = px.scatter(df, x="Gls/90", y="Asts/90", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_xaxes(title_text='Goals/90')
    fig1.update_yaxes(title_text='Assists/90')
    fig1.update_layout(template="plotly_dark",title="Attacking Impact")
    fig1.show()
    fig2 = px.scatter(df, x="Gls/90", y="ShT/90", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_xaxes(title_text='Goals/90')
    fig2.update_yaxes(title_text='Shots on Target/90')
    fig2.update_layout(template="plotly_dark",title="Goalscoring Efficiency")
    fig2.show()
elif choice == "squad":
    sortchoice = dna
    tablechoice = 'dna'
    fig1 = px.scatter(df, x="Age", y="Mins", text="Name", log_x=False, size_max=60)
    fig1.update_traces(textposition='top center')
    fig1.update_layout(height=500)
    fig1.update_yaxes(title_text='Minutes Played')
    fig1.update_xaxes(title_text='Age')
    fig1.update_layout(template="plotly_dark", title="Squad Age Profile")
    fig1.show()
    fig2 = px.scatter(df, x="Wage", y="Mins", text="Name", log_x=False, size_max=60)
    fig2.update_traces(textposition='top center')
    fig2.update_layout(height=500)
    fig2.update_yaxes(title_text='Minutes Played')
    fig2.update_xaxes(title_text='Wages (£)')
    fig2.update_layout(template="plotly_dark",title="Value for Money")
    fig2.show()

# Create html output of dataframe
show = sortchoice.nlargest(10,tablechoice)
html_string = '''
<html>
  <head><title>HTML Pandas Dataframe with CSS</title></head>
  <link rel="stylesheet" type="text/css" href="df_style.css"/>
  <body>
    {table}
  </body>
</html>.
'''

# OUTPUT AN HTML FILE
with open('output.html', 'w',encoding="utf-8") as f:
    f.write(html_string.format(table=show.to_html(classes='mystyle')))
os.startfile('output.html')



# In[ ]:




