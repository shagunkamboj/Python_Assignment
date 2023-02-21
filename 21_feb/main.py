from trial import * 
def main():
    subjects_build = subjectsBuild()
    final = Final(subjects_build)
    Assignments = final.get_subjects()
    Assignments.specification() 
if __name__ == "main":
    main()
        