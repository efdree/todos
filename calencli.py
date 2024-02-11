from datetime import datetime, timedelta
from  colorama import Fore
import re

# Data
id = 0
events = [
  { "id" : (id := id + 1),
    "start_date" : "2023-11-15T10:00:00-05:00",
    "title" : "Ruby Basics 1",
    "end_date" : "2023-11-15T11:00:00-05:00",
    "notes" : "Ruby Basics 1 notes",
    "guests" : ["Teddy", "Codeka"],
    "calendar" : "web-dev" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-15T12:00:00-05:00",
    "title" : "English Course",
    "end_date" : "2023-11-15T13:30:00-05:00",
    "notes" : "English notes",
    "guests" : ["Stephanie"],
    "calendar" : "english" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-16T00:00:00-05:00",
    "title" : "Ruby Basics 2",
    "end_date" : "",
    "notes" : "Ruby Basics 2 notes",
    "guests" : "Andre Codeka",
    "calendar" : "web-dev" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-16T12:45:00-05:00",
    "title" : "Soft Skills - Mindsets",
    "end_date" : "2023-11-15T13:30:00-05:00",
    "notes" : "Some extra notes",
    "guests" : ["Diego"],
    "calendar" : "soft-skills" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-17T00:00:00-05:00",
    "title" : "Ruby Methods",
    "end_date" : "",
    "notes" : "Ruby Methods notes",
    "guests" : ["Diego", "Andre", "Teddy", "Codeka"],
    "calendar" : "tech" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-17T12:00:00-05:00",
    "title" : "English Course",
    "end_date" : "2023-11-15T13:30:00-05:00",
    "notes" : "English notes",
    "guests" : ["Stephanie"],
    "calendar" : "english" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-18T09:00:00-05:00",
    "title" : "Summary Workshop",
    "end_date" : "2023-11-19T13:30:00-05:00",
    "notes" : "A lot of notes",
    "guests" : ["Diego", "Teddy", "Andre", "Codeka"],
    "calendar" : "web-dev" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-18T09:00:00-05:00",
    "title" : "Extended Project",
    "end_date" : "",
    "notes" : "",
    "guests" : [],
    "calendar" : "web-dev" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-19T09:00:00-05:00",
    "title" : "Extended Project",
    "end_date" : "",
    "notes" : "",
    "guests" : [],
    "calendar" : "web-dev" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-19T12:00:00-05:00",
    "title" : "English for Engineers",
    "end_date" : "2023-11-19T13:30:00-05:00",
    "notes" : "English notes",
    "guests" : ["Stephanie"],
    "calendar" : "english" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-20T10:00:00-05:00",
    "title" : "Breakfast with my family",
    "end_date" : "2023-11-20T11:00:00-05:00",
    "notes" : "",
    "guests" : [],
    "calendar" : "default" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-20T15:00:00-05:00",
    "title" : "Study",
    "end_date" : "2023-11-20T20:00:00-05:00",
    "notes" : "",
    "guests" : [],
    "calendar" : "default" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-25T09:00:00-05:00",
    "title" : "Extended Project",
    "end_date" : "",
    "notes" : "",
    "guests" : [],
    "calendar" : "web-dev" },
  { "id" : (id := id + 1),
    "start_date" : "2023-11-26T09:00:00-05:00",
    "title" : "Extended Project",
    "end_date" : "",
    "notes" : "",
    "guests" : [],
    "calendar" : "web-dev" }
]

# Methods

def agenda(data, actual_date):
  # --------Imprimir bienvenida--------
  print("-" * 29 + "Welcome to CalenCLI" + "-" * 30)
  print("\n")
  # --------Mostrar los eventos del array events--------
  today = datetime.strptime(actual_date, "%Y-%m-%dT%H:%M:%S%z")
  # para 7 días
  for i in range(6):
    # *********Definicion de Variables*********

    # Fecha en formato año-mes-diaThora:min:seg-zona
    y_m_d_zone = (today + timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%S%z")
    # Fecha en formato año-mes-dia
    y_m_d = (today + timedelta(days=i)).strftime("%Y-%m-%d")
    # *********Creacion de arrays*********
    # eventos sin horario específico
    e_wo_s = []
    # eventos con horario específico
    e_w_s = []

    # *********Alamacenamiento de eventos en arrays*********
    for hash in data:
      if hash["start_date"] == y_m_d_zone or (hash["start_date"][0: 10] == y_m_d and not hash["end_date"]):
        e_wo_s.append(f"{hash['title']} ({hash['id']})")
      elif hash["start_date"][0: 10] == y_m_d:
        h_start = hash["start_date"][-14:-9]
        h_end = hash["end_date"][-14:-9]
        e_w_s.append(f"{h_start}-{h_end} {hash['title']} ({hash['id']})")
      e_w_s.sort(key=lambda x: x.split()[0].split("-")[0])

    array_calendar = calendar_event(data, e_w_s)
    array_calendar_wo = calendar_event(data, e_wo_s)
    hash_event_calendar = dict(zip(e_w_s, array_calendar))
    hash_event_calendar_wo = dict(zip(e_wo_s, array_calendar_wo))
    print_agenda(today, i, hash_event_calendar, hash_event_calendar_wo)
  
def calendar_event(data, evento):
  array_color = []
  for string in evento:
    hash_color = next((event for event in data if event["id"] == int(string.split("(")[1].rstrip(")"))), None)
    array_color.append(hash_color)
  
  array_calendar = []
  for calendar_hash in array_color:
    array_calendar.append(calendar_hash["calendar"])

  return array_calendar

def print_agenda(today, cont, hash_event_calendar, hash_event_calendar_wo):
  e_w_s = hash_event_calendar
  e_wo_s = hash_event_calendar_wo
  array_calendar = hash_event_calendar.values()
  array_calendar_wo = hash_event_calendar_wo.values()
  day_week = (today + timedelta(cont)).strftime("%a")
  day_month = (today + timedelta(cont)).strftime("%d")
  month = (today + timedelta(cont)).strftime("%b")
  print(f"{day_week} {day_month} {month}", end="  ")
  if not e_w_s and not e_wo_s:
    print(" " * 12, end="No events")  
    
  else:
    #if not e_wo_s : print(" " * 12, end ="")
    colorize_title(array_calendar_wo, e_wo_s, True)
    #if not e_wo_s : print(" " * 12, end ="")
    colorize_title(array_calendar, e_w_s, False)
  
  print("\n")


def choose_action_from_menu():
  action_list = ["list", "create", "show", "update", "delete", "next", "prev", "exit"]
  print("-"*78 + "\n" + f"{' | '.join(action_list)}\n")
  print()
  action = input("action: ").strip()
  while action not in action_list:
    print("Invalid action")
    action = input("action: ").strip()

  return action


def validate_title():
  title = ""
  i = 1
  while not title:
    if i != 1:
        print("Cannot be blank") 
    title = input("title: ").strip()
    i += 1
  
  return title


def validate_start_end():
  valid = False
  schedule = "asd"
  i = 1
  cond4 = False
  while valid == False:
    if not cond4:
      if i != 1:
        print("Cannot end before start")
    elif i != 1:
      print("Format: 'HH:MM HH:MM' or leave it empty")
    schedule = input("start_end: ").strip()
    array = re.sub(" ", ":", schedule).split(":")
    if not array:
      schedule = "00:00 00:00"
      valid = True
    else:
      cond4 = ((int(array[0]) * 60) + int(array[1])) <= ((int(array[2]) * 60) + int(array[3]))
      conds = [not int(number) < 0 and len(number) == 2 and int(number) < 24 if array.index(number) % 2 == 0 else int(number) < 60 for number in array]
    
      valid = all(conds) and cond4
      i += 1
  return schedule


def valid_date():
    date = ""
    condition = False
    i = 1
    array = date.split("-")
    print(array)
    while condition == False:
        if i != 1: 
            print("Type a valid date: YYYY-MM-DD") 
        date = input("date: ").strip(" ")
        array = date.split("-")
        conds = [int(number) > 0 and len(number) >= 2 for number in array]
        condition = all(conds) and len(array) == 3 and len(array[0]) == 4
        i += 1
  
    return date


def show(events):
  id = 0
  while id == 0:
    id = int(input("Event ID: ").strip())
    if id == 0:
      print("Ingress a correct number")
  selected_event = next((event for event in events if event["id"] == id), None)
  h_start = selected_event["start_date"][-14:-9]
  h_end = selected_event["end_date"][-14:-9]
  print(f"date: {selected_event['start_date'][0:10]}")
  print(f"title: {selected_event['title']}")
  print(f"calendar: {selected_event['calendar']}")
  print(f"start_end: {h_start} {h_end}")
  print(f"notes: {selected_event['notes']}")
  print(f"guests: {', '.join(selected_event['guests'])}")

def delete(events):
  id = int(input("Event ID: ").strip())
  selected_event = next((event for event in events if event["id"] == id), None)
  events.remove(selected_event)


def create(events):
  date = valid_date()
  title = validate_title()
  calendar = input("calendar: ").strip()
  if not calendar: calendar = "default" 
  start_end = validate_start_end()
  start_date = f"{date}T{start_end[0: 5]}:00-05:00"
  end_date = f"{date}T{start_end[6: 11]}:00-05:00"
  notes = input("notes: ").strip()
  guests = input("guests: ").strip().split(", ")

  id = len(events)
  hash = { "id" : id + 1, "start_date" : start_date, "title" : title, "end_date" : end_date,
           "notes" : notes, "guests" : guests, "calendar" : calendar }
  
  print(hash)
  events.append(hash)


def update(events):
  id = int(input("Event ID: ").strip())
  selected_index = next((index for index, event in enumerate(events) if event["id"] == id), None)
  date = valid_date()
  title = validate_title()
  calendar = input("calendar: ").strip()
  if not calendar:
    calendar = "default" 
  start_end = validate_start_end()
  start_date = f"{date}T{start_end[0: 5]}:00-05:00"
  end_date = f"{date}T{start_end[6: 11]}:00-05:00"
  notes = input("notes: ").strip()
  guests = input("guests: ").strip().split(", ")
  hash = { "id" : id, "start_date" : start_date, "title" : title, "end_date" : end_date, "notes" : notes,
           "guests" : guests, "calendar" : calendar }
  events[selected_index] = hash


def colorize_title(array_calendar, tasks, no_schedule):
  indentation = ""
  i = 0
  if no_schedule:
    indentation = " " * 12
  else:
    indentation = " " * 12
  list_tasks = list(tasks.keys())    
  while i < len(tasks):
    if i == 0 and len(tasks) == 1:
      print(indentation, end="")
      
    elif i != 0 and len(tasks) > 1:
      print(indentation, end="")

    case_value = list(array_calendar)[i]
    if case_value == "tech":
      print(Fore.RED + f"{list(tasks.keys())[i]}")
    elif case_value == "english":
      print(Fore.MAGENTA + f"{list(tasks.keys())[i]}")
    elif case_value == "soft-skills":
      print(Fore.GREEN + f"{list(tasks.keys())[i]}")
    else:
      print(Fore.WHITE + f"{list(tasks.keys())[i]}")
    
    i += 1
  


# Main Program
d = "2023-11-15T00:00:00-05:00"
agenda(events, d)
action = choose_action_from_menu()
while action != "exit":
  if action == "list":
    agenda(events, d)
  elif action == "create":
    create(events)
  elif action == "show":
    show(events)
  elif action == "delete":
    delete(events)
  elif action == "update":
    update(events)
  elif action == "next":
    d_new = datetime.strptime(d, "%Y-%m-%dT%H:%M:%S%z") + timedelta(7)
    y_m_d_zone = (d_new).strftime("%Y-%m-%dT%H:%M:%S%z")
    agenda(events, y_m_d_zone)
    d = y_m_d_zone
  elif action == "prev":
    d_new = datetime.strptime(d, "%Y-%m-%dT%H:%M:%S%z") - timedelta(7)
    y_m_d_zone = (d_new).strftime("%Y-%m-%dT%H:%M:%S%z")
    agenda(events, y_m_d_zone)
    d = y_m_d_zone

  action = choose_action_from_menu()

print("Thanks for using calenCLI")