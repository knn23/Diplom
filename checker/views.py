from django.shortcuts import render, get_object_or_404
from .models import Task, Solution
from .forms import SolutionForm
import subprocess
import json

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = SolutionForm(request.POST or None)
    result = None

    if request.method == 'POST' and form.is_valid():
        solution = form.save(commit=False)
        solution.task = task

        # Execute user's code
        try:
            process = subprocess.run(['python3', '-c', solution.code], capture_output=True, text=True, timeout=5)
            output = process.stdout.strip()

            # Handle conditions
            if task.conditions:
                conditions = json.loads(task.conditions)

                for condition in conditions:
                    try:
                        expected_output = json.loads(condition['expected_output'])
                    except json.JSONDecodeError:
                        expected_output = condition['expected_output']

                    if str(output) == str(expected_output):
                        solution.is_correct = True
                        result = f"{output}  - Це правильна відповідь!"
                        break
                else:
                    result = f"Неправильно. Очікувалось : {conditions}, Отримано: {output}"
            else:
                # Convert expected output to the appropriate data type
                try:
                    expected_output = json.loads(task.expected_output)
                except json.JSONDecodeError:
                    expected_output = task.expected_output

                if str(output) == str(expected_output):
                    solution.is_correct = True
                    result = "Правильно!"
                else:
                    result = f"Неправильно. Очікувалось: {expected_output}, Отримано: {output}"
        except subprocess.TimeoutExpired:
            result = "Запланований час на обробку програми вийшов"
        except Exception as e:
            result = f"Ошибка: {str(e)}"

    return render(request, 'checker/task_detail.html', {'task': task, 'form': form, 'result': result})

def easy_tasks(request):
    tasks = Task.objects.filter(difficulty='easy')
    return render(request, 'checker/easy_tasks.html', {'tasks': tasks})