from tools import*
import tools

#=============images=======================
data_P=pygame.image.load('Pic\dataP.png')
Q_IMG=pygame.image.load('Pic\Q.png')
T_IMG=pygame.image.load('Pic\True.png')
F_IMG=pygame.image.load('Pic\False.png')

#==========================================
Ques={1:("1+3=?",{1:"2",2:"3",3:"4",4:"1"},3),
      2:("9+1=?",{1:"12",2:"7",3:"6",4:"10"},4),
      3:("4+10=?",{1:"14",2:"13",3:"-14",4:"16"},1),
      4:("6+13=?",{1:"11",2:"19",3:"14",4:"13"},2),
      5:("8+9=?",{1:"17",2:"20",3:"14",4:"10"},1),
      6:("9+11=?",{1:"19",2:"11",3:"20",4:"17"},2),
      7:("5+2=?",{1:"6",2:"5",3:"4",4:"7"},4),
      8:("6+3=?",{1:"7",2:"8",3:"9",4:"10"},3),
      9:("12+4=?",{1:"16",2:"15",3:"14",4:"17"},1),
      10:("10+3=?",{1:"18",2:"13",3:"19",4:"10"},2),
      11:("9-11=?",{1:"-19",2:"-1",3:"-20",4:"-2"},4),
      12:("5-2=?",{1:"6",2:"5",3:"4",4:"3"},4),
      13:("6-3=?",{1:"3",2:"8",3:"9",4:"1"},1),
      14:("12-4=?",{1:"16",2:"8",3:"4",4:"7"},2),
      15:("10-3=?",{1:"8",2:"3",3:"7",4:"10"},3),
      16:("1-3=?",{1:"-2",2:"-3",3:"-4",4:"-1"},1),
      17:("9-1=?",{1:"8",2:"7",3:"6",4:"9"},1),
      18:("4-10=?",{1:"14",2:"-14",3:"-6",4:"6"},3),
      19:("6-13=?",{1:"-11",2:"-7",3:"9",4:"10"},2),
      20:("8-9=?",{1:"-3",2:"2",3:"3",4:"-2"},4),
      21:("3*1=?",{1:"2",2:"3",3:"4",4:"1"},1),
      22:("9*2=?",{1:"12",2:"18",3:"16",4:"10"},4),
      23:("4*5=?",{1:"14",2:"15",3:"20",4:"16"},3),
      24:("6*2=?",{1:"11",2:"12",3:"14",4:"13"},2),
      25:("8*4=?",{1:"24",2:"30",3:"32",4:"10"},3),
      26:("3*3=?",{1:"9",2:"11",3:"12",4:"7"},1),
      27:("5*2=?",{1:"5",2:"13",3:"14",4:"10"},4),
      28:("7*3=?",{1:"23",2:"18",3:"21",4:"20"},3),
      29:("12*4=?",{1:"24",2:"28",3:"23",4:"27"},2),
      30:("10*3=?",{1:"30",2:"33",3:"31",4:"29"},1),
      31:("4/2=?",{1:"3",2:"4",3:"5",4:"2"},4),
      32:("10/2=?",{1:"6",2:"5",3:"4",4:"3"},2),
      33:("9/3=?",{1:"3",2:"8",3:"9",4:"1"},1),
      34:("12/4=?",{1:"6",2:"8",3:"4",4:"7"},3),
      35:("30/3=?",{1:"18",2:"13",3:"7",4:"10"},4),
      36:("14/2=?",{1:"-7",2:"7",3:"13",4:"11"},2),
      37:("9/1=?",{1:"8",2:"7",3:"6",4:"9"},4),
      38:("24/6=?",{1:"-4",2:"4",3:"-6",4:"6"},2),
      39:("33/11=?",{1:"11",2:"7",3:"3",4:"10"},3),
      40:("6/2=?",{1:"3",2:"2",3:"6",4:"4"},1),
      41:("(1/3)+1=?",{1:"2.5",2:"3.3",3:"4.2",4:"1.3"},4),
      42:("(9*2)-3=?",{1:"12",2:"18",3:"16",4:"15"},4),
      43:("(4*5)+0.5=?",{1:"14.4",2:"15.5",3:"20.5",4:"16.5"},3),
      44:("(6*2)-12+0.75=?",{1:"1.75",2:"12.75",3:"0.75",4:"13.75"},3),
      45:("[(8*4)-12]*0.5=?",{1:"15.5",2:"10",3:"32",4:"13"},2),
      46:("[(3*3)/2]+1=?",{1:"5.5",2:"10.5",3:"9.2",4:"4.6"},1),
      47:("[(5*2)-3]*3=?",{1:"21",2:"13.5",3:"23.5",4:"10"},1),
      48:("[30-(7*3)]*3=?",{1:"23",2:"3",3:"6",4:"30"},2),
      49:("[12+(12*2)]/3=?",{1:"14",2:"22",3:"23",4:"12"},4),
      50:("[(10*3)-5]/5=?",{1:"30",2:"23",3:"5",4:"19"},3),
      51:("[-6+(4/2)]+0.5=?",{1:"-13.5",2:"14.4",3:"-4.5",4:"2.6"},3),
      52:("[(10/2)+0.5]*0=?",{1:"6",2:"0",3:"4.5",4:"3.1"},2),
      53:("[-3+(9/3)]+0.4=?",{1:"0.4",2:"8.4",3:"9.4",4:"1.4"},1),
      54:("[-1+(2/4)]-0.5=?",{1:"-1.4",2:"3.5",3:"-1",4:"1"},3),
      55:("[(30/3)+0.6]+0.4=?",{1:"18.6",2:"13.4",3:"10",4:"11"},4),
      56:("[(14/2)-20]*0.5=?",{1:"-7",2:"-3",3:"3",4:"7"},2),
      57:("[(9/2)+0.5]*2=?",{1:"8.5",2:"7.5",3:"12",4:"10"},4),
      58:("[-8+(24/6)]/2=?",{1:"-4",2:"-2",3:"-24",4:"-6"},2),
      59:("[(33/11)-5.5]*2=?",{1:"11",2:"7.5",3:"9",4:"10"},3),
      60:("[[(30*10)+12+20]*0]+0.1+0.3-0.2=?",{1:"0.1",2:"0",3:"0.3",4:"0.2"},1)}



      
#==============(פונקציות שאלות)============

def Question(level):
        time.sleep(2)
        loop= True
        Ans=0
        
        if level==1:
          Q=random.randint(1,20)
        elif level==2:
          Q=random.randint(21,40)
        elif level==3:
          Q=random.randint(41,60)
        while loop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()        

                gameDisplay.blit(Q_IMG,(0,0))
                pygame.draw.rect(gameDisplay, colors['gray_l'],(200,240,400,80))

                
                Message_2(Ques[Q][0],200,240)
                if button_2(Ques[Q][1][1],130,440,125,60,colors['gray_l'],colors['gray'],'1'):
                                Ans=1
                if button_2(Ques[Q][1][2],270,440,125,60,colors['gray_l'],colors['gray'],'2'):
                                Ans=2
                if button_2(Ques[Q][1][3],410,440,125,60,colors['gray_l'],colors['gray'],'3'):
                                Ans=3
                if button_2(Ques[Q][1][4],550,440,125,60,colors['gray_l'],colors['gray'],'4'):
                                Ans=4
                if Ans!=0:
                        if Ans==Ques[Q][2]:
                                gameDisplay.blit(T_IMG,(0,0))
                                pygame.display.update()
                                time.sleep(2) 
                                return True
                        else:
                                gameDisplay.blit(F_IMG,(0,0))
                                pygame.display.update()
                                time.sleep(2) 
                                return False
                pygame.display.update()
                clock.tick(15)
