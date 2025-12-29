import streamlit as st
import os
import json

filename = "data/tasks_list.json"
if os.path.exists(filename):
	with open(filename, 'r') as data_json:
		check_data = data_json.read().strip()
		if not check_data:
                	with open(filename,"w") as data_json:
                        	data_json.write("{}")
else:
	with open(filename, "w") as data_json:
		data_json.write("{}")

st.set_page_config(
	page_title = "Task Manager Project"
)

st.title("Task Manager Project")
st.divider()

st.header("View Tasks")
view_option = st.button("Would you like to view the current list of tasks?")

st.header("Add Tasks")
task_title = st.text_input("Insert the title of the task you would like to add.")
task_desc = st.text_input("Insert the description of the task you would like to add.")
add_option = st.button("Are you sure you would like to add the task?")

st.header("Mark Tasks Complete")
change_status_title = st.text_input("Insert the title of the task you would like to mark complete.")
change_status_option = st.button("Are you sure you would like to mark the task complete?")

###

if view_option:
	with open(filename, 'r') as data_json:
		check_data = data_json.read().strip()
		if check_data == "{}":
			st.warning("No tasks in list!")
		else:
			display_data = json.load(data_json)
			st.json(display_data)

if add_option:
	data_insert = {task_title: [task_desc, "In Progress"]}
	if not task_desc:
		st.warning("Tasks included must have a title!")
	else:
		with open(filename, "r+") as data_json:
			data = json.load(data_json)
			data[task_title] = [task_desc, "In Progress"]
		with open(filename, "w") as data_json:
			json.dump(data, data_json, indent = 4)
		st.success("Task added!")

if change_status_option:
	if not change_status_title:
		st.warning("No tasks to mark complete!")
	else:
		st.success("Task marked complete!")
		with open (filename,"r") as data_json:
			lines = json.load(data_json)
			for i in lines:
				if  (i == remove_title):
					lines[i][1] = "Task Completed"
		with open (filename, "w") as data_json:
			json.dump(lines, data_json, indent = 4)
