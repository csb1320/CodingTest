board1= [i for i in range(0,41,2)]
board2 = [0,2,4,6,8,10,13,16,19,25,30,35,40] # 12 
board3 = [0,2,4,6,8,10,12,14,16,18,20,22,24,25,30,35,40] # 16 
board4 = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,28,27,26,25,30,35,40] # 22 
board = [board1,board2,board3,board4]

answer = 0
def dfs(save_horse,command,index,score):
    if index == 10 : 
        global answer         
        answer = max(answer,score)
        return 
    
    for h in range(4): 
        if save_horse[h][0] == -1 :
            continue 
        save_horse[h][1] += command[index] 

        hx,hy =save_horse[h][0],save_horse[h][1]

        if hy >= len(board[hx]) :
            save_horse[h][0] = -1 
            dfs(save_horse,command,index+1,score)
            save_horse[h][0] = hx 
            save_horse[h][1] -= command[index]
        else : 
            if hx ==0 and board[hx][hy] % 10 == 0 and board[hx][hy] != 40 :
                save_horse[h][0] += board[hx][hy] // 10 

            is_duple = False 
            for i in range(4): 
                if i == h :
                    continue 
                cx,cy = save_horse[i][0], save_horse[i][1] 
                if cx == -1 :
                    continue
                if (hx!= 0 and cx!=0) and ((cy==hy and board[cx][cy] == 30 and board[hx][hy] == 30) or (board[cx][cy] == 35 and board[hx][hy] == 35)) :
                    is_duple = True 
                    break
                if save_horse[i] == save_horse[h] or (board[cx][cy] == 25 and board[hx][hy] == 25) or (board[cx][cy] == 40 and board[hx][hy] == 40 ): 
                    is_duple = True 
                    break 
            if is_duple : 
                save_horse[h][0] = hx
                save_horse[h][1] -= command[index]
                continue 
            dfs(save_horse,command,index+1, score+board[save_horse[h][0]][save_horse[h][1]])
            save_horse[h][0], save_horse[h][1] = hx, hy - command[index]
        if index == h: 
            break 

if __name__ == "__main__":
    command = list(map(int,input().split())) 
    horse = [[0,0]for _ in range(4)]
    dfs(horse, command, 0, 0)
    print(answer)