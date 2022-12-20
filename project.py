import hashlib
from typing import List


def signup():
    status = input("Hi, are you a (f)reelancer or a (c)lient?" + "\n")
    if status == "f":
        username = input("Enter freelancer username: ")
        email = input("Enter Email: ")
        id=input("Enter your id : ")
        phone_number=input("Enter your Phone Number : ")
        national_id=input("Enter Your National Id : ")
        password = input("Enter password: ")

        while 1:
            conf_pwd = input("Confirm password: ")
            if conf_pwd == password:
                enc = conf_pwd.encode()
                hash1 = hashlib.md5(enc).hexdigest()
                with open("freelancers.txt", "a")as f:
                    f.write(username + "\n")
                    f.close()
                with open(username+".txt", "w")as f:
                    f.write(username + "\n")
                    f.write(hash1)
                f.close()
                with open(username+"_profile.txt","w") as f:
                    f.write(username + "\n")
                    f.write(hash1+"\n")
                    f.write(email + "\n")
                    f.write(id + "\n")
                    f.write(phone_number + "\n")
                    f.write(national_id + "\n")
                f.close()
                print("You have registered successfully!")
                break
            else:
                print("Password is not same as above, please input again. \n")
    elif status == "c":
        username = input("Enter Client username: ")
        email = input("Enter Email: ")
        id = input("Enter your id : ")
        password = input("Enter Password: ")
        while 1:
            conf_pwd = input("Confirm password: ")
            if conf_pwd == password:
                enc = conf_pwd.encode()
                hash1 = hashlib.md5(enc).hexdigest()
                with open("client.txt", "w") as f:
                    f.write(username + "\n")
                    f.write(hash1)
                f.close()
                with open(username+"_profile.txt","w") as f:
                    f.write(username + "\n")
                    f.write(hash1+"\n")
                    f.write(id + "\n")
                    f.write(email + "\n")

                print("You have registered successfully!")
                break
            else:
                print("Password is not same as above, please input again.\n")


def login():
    attempts = 4
    global f_username
    status = input("Are you a (f)reelancer or a (c)lient ?" + "\n")
    if status == "f":
        while attempts >= 0:
            f_username = input("Enter username: ")
            password = input("Enter password: ")
            auth = password.encode()
            auth_hash = hashlib.md5(auth).hexdigest()
            with open(f_username+".txt", "r") as f:
                stored_f_username, stored_password = f.read().split("\n")
            f.close()
            if f_username == stored_f_username and auth_hash == stored_password:
                print("Logged in Successfully!")
                freelancer_page()
                break
            else:
                print("Login failed!, you have ", attempts , " attempts to try again\n")
                attempts=attempts-1
        if(attempts<0):
            print("you can't login, try creating account")
            signup()

    elif status == "c":
        while attempts >=0:
            username = input("Enter username: ")
            password = input("Enter password: ")
            auth = password.encode()
            auth_hash = hashlib.md5(auth).hexdigest()
            with open("client.txt", "r") as f:
                stored_corp_username, stored_corp_password = f.read().split("\n")
            f.close()
            if username == stored_corp_username and auth_hash == stored_corp_password:
                print("Logged in Successfully!")
                corp_page()
                break
            else:
                print("Login failed!, you have ",attempts," attempts to try again\n")
                attempts=attempts-1
            if attempts < 0:
                cr_account = input(print("you can't login, would try creating an account?"))
                if cr_account == "y":
                    signup()
                else:
                    break

def corp_page():
    with open("client.txt", "r") as f:
        stored_username, stored_password= f.read().split("\n")
        f.close()
        username = stored_username
        corp_chosen = input("Hi " + username + " Do you want to (l)ist a job or (v)iew applicants?")
        if corp_chosen == "l":
            num = int(input("Enter number of jobs: "))
            i = 1
            j = 1
            while (i<= num and j <= num):
                print("job",i, ":")

                title = input("Enter job title: \n")
                id = input("Enter job id: \n")
                required_skills =input ("Enter required skills: \n")
                job_describ =input("Enter job description: \n ")
                with open("jobs.txt", "r")as f:
                    xlines = len(f.readlines())
                    f.close()
                if xlines == 0:
                    f = open("Jobs.txt","w")
                    f.write(title +"\n")
                else:
                    f = open("jobs.txt", "a")
                    f.write(title + "\n")

                file_Name = title + ".txt"
                x = open(file_Name, "a")
                x.write("Title: " + title + "\n")
                x.write("id: " + id + "\n")
                x.write("Required skills: " + required_skills + "\n")
                x.write("Job describtion: " + job_describ )
                j = j + 1
                i = i + 1


        elif corp_chosen == "v":
            with open("freelancers.txt", "r")as f:
                usernames = f.readlines()
                how_many_usernames = len(f.readlines())
                f.close()
            print("Hi, these applicants have applied to a job: \n")
            print(*usernames, sep =", ")
            username_chosen = input("Which one do you want to see their application?")
            user_job_applied = username_chosen + "_job_applied.txt"
            user_description = username_chosen + "_description.txt"
            with open(user_job_applied, "r")as f:
                job_applied = f.read()
                f.close()
            with open(user_description, "r")as f:
                applicant_description = f.read()
                f.close()
            print(username_chosen + " has applied to " + job_applied)

            print(username_chosen + "'s bio is: " + "\n" +applicant_description + "\n")
            username_job_status = username_chosen + "_job_status.txt"
            job_status_1 = input("Wanna accept this application? (y/n): ")
            if job_status_1 == "y":
                job_status = "Accepted"
                with open(username_job_status, "w") as f:
                    f.write(job_status)
                    f.close()

            else:
                job_status = "Not Accepted"
                with open(username_job_status, "w") as f:
                    f.write(job_status)
                    f.close()



def freelancer_page():
    zero = 0
    global stored_f_username
    counter = 0
    check_job = 0
    lines = 0

    with open(f_username+".txt", "r") as f:
        stored_f_username, stored_password = f.read().split("\n")
        f.close()
        username = stored_f_username
        print("Hi " + username + " there are some jobs available. Do you want to see them?\n")
        viewjobs = input("(y)es, or (n)o\n")
        if viewjobs == "y":
            file=open("jobs.txt","r")
            print(file.read())
            file.close()
            search = input("Please Enter Title Job : \n")
            job_applied= search
            with open(job_applied+ ".txt", "r") as f:
                print(f.read())
                f.close()
        else:
            pass
        job_apply = input("Do you want to apply for a (j)ob? or do you want to see job (s)tatus?" + "\n")
        while job_apply == "j":
            applicant_description = input("Please inter your bio, skills, and social numbers: " + "\n")
            applicant_description_file = username + "_description.txt"
            with open(applicant_description_file, "w")as f:
                f.write(applicant_description + "\n")
                f.close()
            i = int(input("Please enter job's ID " + "\n"))
            i_real = i-1
            job_applied_username = username + "_job_applied.txt"
            with open("jobs.txt", "r")as f:
                job_applied_name = f.readlines()[i_real]
                f.close()
            with open(job_applied_username, "w")as f:
                f.write(job_applied_name + "\n")
                f.close()
            print("Job request sent successfully !")
            break
        while job_apply == "s":
            user_job_status = username +"_job_status.txt"
            with open(user_job_status, "r") as f:
                job_status = f.read()
                f.close()
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
