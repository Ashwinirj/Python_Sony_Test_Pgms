class UserMainCode(object):
    @classmethod
    def isBalanced(cls):
        '''
        input1: String
        Expected return type: Boolean
        '''
        #input1= input("Enter string of brackets")
        input1= "{[()]}"
        len_string = len(input1)
        #print(len_string)
        for i in range(len_string):
            print(input1[i])
            print(input1[len_string-1])
            if (input1[i]==input1[len_string-1]):
                print("Balanced")
                return True
            else:
                return False

check = UserMainCode()
check.isBalanced()