// import { TaskURL } from "./utility";



function genRequest(method, data) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]')?.value
    return {
        method,
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify(data)
    }
}


function getFormData({ id, form }) {

    if (form == undefined || !(form instanceof HTMLFormElement)) {
        console.warn("argument form cannot be null. provide a HTMLFormElement type Object");
    }
    else if (id === undefined || typeof (id) !== 'string') {
        console.warn("argument id must be a string. provide a id of html form element as sting");
    }

    if (form != null && form instanceof HTMLFormElement) {
        return Object.fromEntries(new FormData(form).entries())
    }
    else if (id != null && typeof (id) === "string") {

        return Object.fromEntries(new FormData(document.forms[id]).entries())
    }
    else {
        return {}
    }
}


function updateTaskCompleteStatus(req) {

    console.log("Fetching Request: ", req)

    return fetch(TaskURL.UPDATE_TASK, req)

        .then(response => {
            if (!response.ok) {
                throw new Error(response.statusText)
            }
            return response.json()
        })

        .then(json => {
            if (json?.status === "success") {
                console.log("Task updated successfully");
            }

        })
        .catch(error => {
            console.error('Error:', error);
        })

}


function addNewTask(req) {
    console.info("Sending data to server: ", req)

    return fetch(TaskURL.ADD_TASK, req)

        .then(response => {
            if (!response.ok) {
                response.json()
                    .then(json => {
                        console.error(json.message)
                        console.error(json.details)
                    })
                throw new Error(response.statusText)
            }
            return response.json()
        })

        .then(json => {
            if (json?.status === "success") {
                console.log("Task Created successfully");
            }

        })
        .catch(error => {
            console.error('Error:', error);
        })

}


function loadUpdateCheckHandler() {
    const taskInputCheck = [...document.querySelectorAll('[data-action-type="task-item-check"]')]
    taskInputCheck.forEach((taskInput) => {
        taskInput.onclick = handleTaskCheckBoxClick
    })
}

// ==================================== event handlers =======================


const handleAddTaskFormSubmit = (e) => {
    e.preventDefault()
    console.log(e)
    const form = e.target
    const formData = getFormData({ form })
    addNewTask(genRequest("POST", formData))
}

const handleTaskCheckBoxClick = (e) => {

    const data = {
        taskId: e.target.dataset.id,
        isCompleted: e.target.checked,
    }

    updateTaskCompleteStatus(genRequest("PATCH", data))
}


// ===================================
