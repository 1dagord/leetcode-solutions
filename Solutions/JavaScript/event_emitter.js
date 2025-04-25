/*
    [MEDIUM]
    2694. Event Emitter

    Concepts:
    - classes

    Stats:
        Runtime | 38 ms     [Beats 83.88%]
        Memory  | 53.32 MB  [Beats 85.67%]
*/

class EventEmitter {
    constructor() {
        // eventName |-> Array of functions
        this.events = new Map();
    }

    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (this.events.has(eventName))
            this.events.get(eventName).push(callback);
        else
            this.events.set(eventName, [callback]);

        return {
            unsubscribe: () => {
                // remove function from eventName mapping
                const idx = this.events.get(eventName).indexOf(callback);
                this.events.get(eventName).splice(idx, 1);
                // if no functions mapped to eventName, delete
                if (!this.events)
                    this.events.delete(eventName);
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const output = [];
        if (this.events.has(eventName))
        this.events.get(eventName).forEach((func) => {
            output.push(func(...args));
        });
        return output;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */