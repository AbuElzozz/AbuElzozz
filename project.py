import hashlib


def signup():                                                             # if not have account  before
    status = input("Hi, are you a (f)reelancer or a (c)lient?" + "\n")    # Check if freelancer or client to direct for each page
    if status == "f":
        username = input("Enter freelancer username: ")
        email = input("Enter Email: ")
        id=input("Enter your id : ")
        phone_number=input("Enter your Phone Number : ")
        national_id=input("Enter Your National Id : ")
        password = input("Enter password: ")

        while 1:                                                          # confirm if same two password Entered
            conf_pwd = input("Confirm password: ")
            if conf_pwd == password:
                enc = conf_pwd.encode()                               # change password from number to encrypation hexanumber
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
    attempts = 4                # idea if enter username or password 5 times wrong will switch to sign up page again
    global f_username
    status = input("Are you a (f)reelancer or a (c)lient ?" + "\n")
    if status == "f":
        while attempts >= 0:
            f_username = input("Enter username: ")
            password = input("Enter password: ")
            auth = password.encode()
            auth_hash = hashlib.md5(auth).hexdigest()
            with open(f_username+".txt", "r") as f:                # open user_file to take username and passowrd in which taken in signup page to confirm  registertion
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
            with open("client.txt", "r") as f:              # open user_file to take username and passowrd in which taken in signup page to confirm  registertion
                stored_c_username, stored_c_password = f.read().split("\n")
            f.close()
            if username == stored_c_username and auth_hash == stored_c_password:
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
    with open("client.txt", "r") as f:     #open user file to get his name and use it in converstion after
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
                with open("jobs.txt", "a")as f:
                    f.write(title + "\n")
                    f.close()

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
                f.close()
            print("Hi, these applicants have applied to a job: \n")
            print(*usernames, sep =",")
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
    global job_applied
    global stored_f_username
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
            job_applied_username = username + "_job_applied.txt"
            with open(job_applied_username, "w")as f:
                f.write(job_applied + "\n")
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
