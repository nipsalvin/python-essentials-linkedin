class Duck:
    sound = "Quaaaaaaack!"
    walking = "Walks like donald duck"

    def quack(self):
        #print("Quaaack!")
        print(self.sound)

    def walks(self):
        #print("Walks like a duck")
        print(self.walking)

def main():
    donald = Duck()
    donald.quack() #calling method quack
    donald.walks() #calling method walks

if __name__ == "__main__":main()