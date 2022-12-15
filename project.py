import hashlib
from typing import List

a = ""
b = ""
job_status = ""


def signup():
    status = input("Hi, are you a (f)reelancer or a (c)orporation?" + "\n")
    if status == "f":
        username = input("Enter freelancer username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        while 1:
            conf_pwd = input("Confirm password: ")
            if conf_pwd == password:
                enc = conf_pwd.encode()
                hash1 = hashlib.md5(enc).hexdigest()
                with open(username+".txt", "w") as f:
                    f.write(username + "\n")
                    f.write(hash1)
                f.close()
                print("You have registered successfully!")
                break
            else:
                print("Password is not same as above, please input again. \n")
    elif status == "c":
        username = input("Enter corporation username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        while 1:
            conf_pwd = input("Confirm password: ")
            if conf_pwd == password:
                enc = conf_pwd.encode()
                hash1 = hashlib.md5(enc).hexdigest()
                with open("corp_credentials.txt", "w") as f:
                    f.write(username + "\n")
                    f.write(hash1)
                f.close()
                print("You have registered successfully!")
                break
            else:
                print("Password is not same as above, please input again.\n")

def login():
    play = 4
    global f_username
    status = input("Are you a (f)reelancer or a (c)orporation?" + "\n")
    if status == "f":
        while play>=0:
            f_username = input("Enter username: ")
            password = input("Enter password: ")
            auth = password.encode()
            auth_hash = hashlib.md5(auth).hexdigest()
            with open(f_username+".txt", "r") as f:
                stored_fren_username, stored_password = f.read().split("\n")
            f.close()
            if f_username == stored_fren_username and auth_hash == stored_password:
                print("Logged in Successfully!")
                freelancer_page()
                break
            else:
                print("Login failed!, you have " , play , " attempts to try again\n")
                play=play-1
        if(play<0):
            print("you can't login, try creating account")
            signup()

    elif status == "c":
        while play >=0:
            username = input("Enter username: ")
            password = input("Enter password: ")
            auth = password.encode()
            auth_hash = hashlib.md5(auth).hexdigest()
            with open("corp_credentials.txt", "r") as f:
                stored_corp_username, stored_corp_password = f.read().split("\n")
            f.close()
            if username == stored_corp_username and auth_hash == stored_corp_password:
                print("Logged in Successfully!")
                corp_page()
                break
            else:
                print("Login failed!, you have ",play," attempts to try again\n")
                play=play-1
            if play <0:
                print("you can't login, try creating account")
                signup()

def corp_page():
    with open("corp_credentials.txt", "r") as f:
        stored_username, stored_password= f.read().split("\n")
        f.close()
        username = stored_username
        corp_chosen = input("Hi " + username + " Do you want to (l)ist a job or (v)iew applicants?")
        if corp_chosen == "l":
            num = int(input("Enter number of jobs: "))
            i = 1
            j = 1
            while (i<= num and j <= num) :
                print("job",i)

                title = input("Enter job title: ")
                id = input("Enter job id: ")
                required_skills =input ("Enter required skills: ")
                job_describ =input("Enter job describtion: ")

                f = open("Jobs.txt","w")
                f.write("Title: "+ title +"\n")
                f.write("id: " + id + "\n")
                f.write("Required skills: " + required_skills + "\n")
                f.write("Job describtion: " + job_describ + "\n\n")


                fileName = title + ".txt"
                x = open(fileName, "a")
                x.write("Title: " + title + "\n")
                x.write("id: " + id + "\n")
                x.write("Required skills: " + required_skills + "\n")
                x.write("Job describtion: " + job_describ + "\n\n")
                j = j + 1
                i = i + 1


        elif corp_chosen == "v":
            with open("job_applied.txt", "r")as f:
                job_applied = f.read()
                f.close()
            with open("applicant_description.txt", "r")as f:
                applicant_description = f.read()
                f.close()
            with open(stored_fren_username+".txt", "r") as f:
                stored_username = f.read().split("\n")
                f.close()
            print(stored_username[0] + " has applied to " + job_applied)

            print(stored_username[0] + "'s bio is: " + "\n" +applicant_description + "\n")
            job_status_1 = input("Wanna accept this application? (y/n): ")
            if job_status_1 == "y":
                job_status = "Accepted"
                with open("job_status.txt", "w") as f:
                    f.write(job_status)
                    f.close()

            else:
                job_status = "Not Accepted"
                with open("job_status.txt", "w") as f:
                    f.write(job_status)
                    f.close()



def freelancer_page():
    zero = 0
    global stored_fren_username
    global job_applied
    with open(f_username+".txt", "r") as f:
        stored_fren_username, stored_password = f.read().split("\n")
        f.close()
        username = stored_fren_username
        print("Hi " + username + " there are some jobs available. Do you want to see them?\n")
        viewjobs = input("(y)es, or (n)o\n")
        if viewjobs == "y":
            search=input("Please Enter Title Job : \n")
            job_applied=search
            with open(job_applied+".txt", "r") as f:
                print(f.read())
                f.close()
        pass
        job_apply = input("Do you want to apply for a (j)ob? or do you want to see job (s)tatus?" + "\n")
        while job_apply == "j":
            applicant_description = input("Please inter your bio: " + "\n")
            with open("applicant_description.txt", "w")as f:
                f.write(applicant_description + "\n")
                f.close()
                with open("job_applied.txt", "w") as f:
                    f.write(job_applied)
                    f.close()
            print("Job request sent successfully !")
            break
        with open("job_status.txt", "r")as f:
            job_status = f.read()
            f.close()
        while job_apply == "s":
            print("you " + "have been " + job_status + " to your job!" + "\n")
            break



while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")
