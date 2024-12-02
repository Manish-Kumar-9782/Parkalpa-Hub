const DateFormat = countdown.DAYS | countdown.HOURS | countdown.MINUTES

const DateStatus = Object.freeze({
    OK: "ok",
    OVERDUE: "overdue",
    WARNING: "warning"
})


function getProject(pid) {
    return document.getElementById(pid)
}

function getProjectList() {
    return document.querySelectorAll("[data-type='project']")
}

function getProjectDates({ pid, proj }) {

    let project;

    if (proj instanceof HTMLDivElement && proj.dataset.type === "project") {
        project = proj
    }
    else if (typeof pid === "string") {
        project = getProject(pid)
    }

    let dates = [...project.querySelectorAll("[datetime]")]

    return dates.reduce((result, _date) => {

        let dateTime = null;

        if (_date.dateTime != "") {
            dateTime = new Date(_date.dateTime)
        }

        return { ...result, [_date.dataset.name]: dateTime }
    }, {})
}


function initCountdown(ts, pid, status) {
    let proj = getProject(pid)
    let str;

    if (status) {

        let state = {};

        if (status === DateStatus.OK) {
            state.name = "Remaining"
            state.btClass = "info"
        }
        else if (status === DateStatus.WARNING) {
            state.name = "Due In"
            state.btClass = "warning"
        }
        else if (status === DateStatus.OVERDUE) {
            state.name = "Over Due"
            state.btClass = "danger"
        }

        str = `<strong class='text-${state.btClass}'>${state.name}: </strong>`
            + ts.toHTML(`strong class='text-${state.btClass}-emphasis'`)
    }
    else {
        str = ts.toHTML("strong")
    }

    return proj.innerHTML = str
}


function loadTimer() {
    let projectList = getProjectList()

    projectList.forEach((project) => {
        let dates = getProjectDates({ pid: project.id, proj: project })
        let currentTime = new Date()

        let status;


        if (dates.endDate > currentTime) {

            let ts = countdown(currentTime, dates.endDate, countdown.DAYS)
            if (ts.days >= 2) {
                status = DateStatus.WARNING
            }
            else {
                status = DateStatus.OK
            }

        }
        else {
            status = DateStatus.OVERDUE
        }

        countdown(dates.endDate, (ts) => initCountdown(ts, `${project.id}-countdown`, status), DateFormat)
    })
}