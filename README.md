# self_learning_ping_pong
Source code of ping pong game which learns to play the game by user gameplay using machine learning.

IN UPDATE METHOD OF THE PADDLE CLASS 
  CODE TO USE WHEN YOU WANT THE MACHINE TO PLAY
        pda=np.array([[ballplay.x,ballplay.y,ballplay.vx,ballplay.vy]])
        model.predict([X.to_numpy()[0],X.to_numpy()[0]])
        self.y=int(model.predict(pda)
  CODE TO USE WHEN YOU WANT TO PLAY THROUGH MOUSE
        self.y=pygame.mouse.get_pos()[1]
        
        
  WHILE USING ONE OF ABOVE ....COMMENT THE OTHER ONE TO AVOID ERRORS..
  
  IN THE PROJECT I HAVE ALREADY TRAINED THE DATASET BY PLAYING SOME NUMBER OF TIMES.
  YOU CAN USE YOUR OWN PLAYING STYLE TO TRAIN .
  BY STORING THE CO-ORDINATES OF BALL AND PADDLE WHILE PLAYING AND THEN READING THAT DATASET TO TRAIN THE MODEL..
  
  THANK YOU.
  HAVE FUN
