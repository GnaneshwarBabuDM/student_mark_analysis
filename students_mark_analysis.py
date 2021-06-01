import csv
import sys

def calc_top_students(total_marks):
    # Function to retrive the top three toppers

    first_mark, second_mark, third_mark = 0, 0, 0
    first_mark_name, second_mark_name, third_mark_name ='','',''

    for k, v in total_marks.items():
        if v > first_mark:
            third_mark = second_mark
            third_mark_name = second_mark_name
            second_mark = first_mark
            second_mark_name = first_mark_name
            first_mark = v
            first_mark_name = k

        elif v > second_mark and v != first_mark:
            third_mark = second_mark
            third_mark_name = second_mark_name
            second_mark = v
            second_mark_name = k

        elif v > third_mark and v != second_mark and v != first_mark:
            third_mark = v
            third_mark_name = k

    return first_mark_name, second_mark_name, third_mark_name

def student_data_analysis(students_marksheet):
    # Function to get the toppers in each subjects
    
    maths, biology, english, physics, chemistry, hindi = 0, 0, 0, 0, 0, 0
    total_marks = {}
    with open(students_marksheet, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:

            if int(dict(row)['Maths'])> maths:
                maths = int(dict(row)['Maths'])
                maths_top_name = dict(row)['Name']
                
            if int(dict(row)['Biology'])> biology:
                biology = int(dict(row)['Biology'])
                bio_top_name = dict(row)['Name']
                
            if int(dict(row)['English'])> english:
                english = int(dict(row)['English'])
                eng_top_name = dict(row)['Name']
                
            if int(dict(row)['Physics'])> physics:
                physics = int(dict(row)['Physics'])
                physics_top_name = dict(row)['Name']
                
            if int(dict(row)['Chemistry'])> chemistry:
                chemistry = int(dict(row)['Chemistry'])
                chem_top_name = dict(row)['Name']
                
            if int(dict(row)['Hindi'])> hindi:
                hindi = int(dict(row)['Hindi'])
                hindi_top_name = dict(row)['Name']
                
            total = int(dict(row)['Maths'])+\
                        int(dict(row)['Biology'])+\
                            int(dict(row)['English'])+\
                                int(dict(row)['Physics'])+\
                                    int(dict(row)['Chemistry'])+\
                                        int(dict(row)['Hindi'])   
        
            total_marks[dict(row)['Name']] = total
            first_mark_name, second_mark_name, third_mark_name = calc_top_students(total_marks)
            # toppers = sorted(total_marks, key=total_marks.get, reverse=True)[:3]
                
    print('Topper in Maths is {0}'.format(maths_top_name))
    print('Topper in Biology is {0}'.format(bio_top_name))
    print('Topper in English is {0}'.format(eng_top_name))
    print('Topper in Physics is {0}'.format(physics_top_name))
    print('Topper in Chemistry is {0}'.format(chem_top_name))
    print('Topper in Hindi is {0}'.format(hindi_top_name))
    print('Best students in the class are {0}, {1}, {2}'.format(first_mark_name, second_mark_name, third_mark_name))

if __name__ == "__main__":
    students_marksheet = sys.argv[1]
    student_data_analysis(students_marksheet)