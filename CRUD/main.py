import sys
import csv
import os

COURSE_TABLE='.courses.csv'
COURSE_SCHEMA =['name','instructed_by','dificulty']
courses = []

def _initialize_courses_from_storage():
	with open(COURSE_TABLE, mode='r') as f:
		reader= csv.DictReader(f,fieldnames=COURSE_SCHEMA)


		for row in reader:
			courses.append(row)


def _save_courses_to_storage():
	tmp_table_name ='{}.tmp'.format(COURSE_TABLE)
	with open (tmp_table_name,mode='w') as f:
		writer=csv.DictWriter(f,fieldnames=COURSE_SCHEMA)
		writer.writerows(courses)

		os.remove(COURSE_TABLE)
		f.close()
		os.rename(tmp_table_name,COURSE_TABLE)


def create_course(course):
	global courses

	if course not in courses:
		courses.append(course)
	else:
		print('course already in course\'s list')


def list_courses():
	print('uid |           name         | instructed_by  | dificulty ')
	print('*' * 50)

	for idx, course in enumerate(courses):
		print('{uid} | {name} | {instructed_by} | {dificulty}'.format(
			uid=idx, 
			name=course['name'], 
			instructed_by=course['instructed_by'], 
			dificulty=course['dificulty']))


def update_course(course_id, updated_course):
	global courses
	if len(courses) - 1 >= course_id:
		courses[course_id] = updated_course
	else:
		print('course not in course\'s list')



def delete_course(course_id):
	global courses

	for idx, course in enumerate(courses):
		if idx == course_id:
			del courses[idx] 
			break


def search_course(course_name):
	for course in courses:
		if course['name'] != course_name:
			continue
		else:
			return True


def _get_course_field(field_name, message='What is the course {}?'):
	field = None

	while not field:
		field = input(message.format(field_name))

	return field


def _get_course_from_user():
	course = {
		'name': _get_course_field('name'),
		'instructed_by': _get_course_field('instructed_by'),
		'dificulty': _get_course_field('dificulty'),
	}

	return course


def _print_welcome():
	print('WELCOME TO PLATZI COURSES')
	print('*' * 50)
	print('What would you like to do today?:')
	print('[C]reate course')
	print('[L]ist courses')
	print('[U]pdate course')
	print('[D]elete course')
	print('[S]earch course')


if __name__ == '__main__':
	_initialize_courses_from_storage()
	_print_welcome()
	
	command = input()
	command = command.upper()

	if command == 'C':
		course = _get_course_from_user()

		create_course(course)
	elif command == 'L':
		list_courses()
	elif command == 'U':

		course_id = int(_get_course_field('id'))
		updated_course = _get_course_from_user()

		update_course(course_id, updated_course)
	elif command == 'D':
			course_id = int(_get_course_field('id'))

			delete_course(course_id)
	elif command == 'S':
			course_name = _get_course_field('name')
			found = search_course(course_name)
			if found:
				print('The course is in the course\'s list')
			else:
				print('The course: {} is not in our course\'s list'.format(course_name))
	else:
		print('Invalid command')

	_save_courses_to_storage()
