import streamlit as st
import pandas as pd
import os
import json

st.set_page_config(
	page_title = "Task Manager Project"
)

if "tasks" not in st.session_state:
	st.session_state.tasks = []

st.title("Task Manager Project")
st.divider()

st.header("View Tasks")
view_option = st.button("Would you like to view the current list of tasks?")

st.header("Add Tasks")
task_title = st.text_input("Insert the title of the task you would like to add.")
task_desc = st.text_input("Insert the description of the task you would like to add.")
add_option = st.button("Are you sure you would like to add the task?")

st.header("Mark Tasks Complete")
remove_title = st.text_input("Insert the title of the task you would like to remove.")
remove_option = st.button("Are you sure you would like to mark the task complete?")

#if view_option: 
	#if not st.session_state.tasks:
		# petersburg 
