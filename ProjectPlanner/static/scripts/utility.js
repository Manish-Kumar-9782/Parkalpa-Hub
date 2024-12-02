const TaskURL = Object.freeze({
    UPDATE_TASK: '/project/api/tasks/update',
    ADD_TASK: '/project/api/tasks/add'
})


class FormX {
    constructor({ id, form, infoTextClass = 'form-text' }) {
        this.__extractForm__({ id, form })
        // input container Role
        this._icAttr = 'data-input-name'
        this.infoTextClass = infoTextClass
        this._iContainers = {}
        this.__extractInputContainers__()

    }

    __extractForm__({ id, form }) {

        if (id == null && form == null) {
            throw new Error('id or form must be provided')
        }

        // Now one of them must be provided
        if (id != null && typeof (id) != 'string') {
            throw new Error('id must be a string')
        }
        else if (form != null && !(form instanceof HTMLFormElement)) {
            throw new Error("form must be an instance of HTMLFormElement")
        }

        // Now we are assured that we have either id or form and valid inputs

        if (id != null) {
            form = document.forms[id]
            if (form == null) {
                throw new Error(`form with id ${id} does not exist`)
            }
            else if (!form instanceof HTMLFormElement) {
                throw new Error(`form with id ${id} is not an instance of HTMLFormElement`)
            }

            this.form = form
            this._FormData = new FormData(form)
        }
    }


    __extractInputContainers__() {
        let iboxes = [...this.form.querySelectorAll(`[${this._icAttr}]`)]

        iboxes.reduce((inputs, item) => {
            // console.log(item.dataset.inputName, item, inputs)
            inputs[item.dataset.inputName] = item
            return inputs
        }, this._iContainers)



        console.log(this._iContainers)
        if (this._iContainers.length == 0) {
            console.warn("No Input Field Container found..!")
        }

    }

    __selectTextItem__(key) {
        let item = this._iContainers[key].querySelector(".form-text")
        if (!item) {
            console.warn(`No text item found for key ${key}`)
            return null
        }
        return item
    }

    getData() {
        if (this._FormData != null) {
            return Object.fromEntries(this._FormData.entries())
        }
        else {
            this._FormData = new FormData(this.form)
            return this.getData()
        }
    }

    setInfoText(key, message, type = "info") {
        const textItem = this.__selectTextItem__(key)
        if (textItem) {
            textItem.innerText = message
            textItem.classList.add(`text-${type}`)
        }
    }


}