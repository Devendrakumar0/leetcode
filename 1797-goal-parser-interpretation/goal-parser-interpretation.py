class Solution:
    def interpret(self, command: str) -> str:
        x_list = list(command)
        i=0
        while i<len(x_list):
            if x_list[i]=="(" and i + 1 < len(x_list) and x_list[i+1]==")":
                x_list[i]="o"
                x_list.pop(i+1)
            elif x_list[i] == "(" or x_list[i]==")":
                x_list.pop(i)
            else:
                i+=1
        command = ''.join(x_list)
        return command
        