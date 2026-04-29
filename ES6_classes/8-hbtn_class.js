export default class HolbertonCourse {
    constructor(size, location) {
        this._size = size;
        this._location = location;
    }
    get size() {
        return this._size;
    }

    get location() {
        return this._location;
    }
    set size(value) {
        if (typeof value !== 'number') {
            throw new TypeError('Size must be a number');
        }
        this._size = value;
    }

    set location(value) {
        if (typeof value !== 'string') {
            throw new TypeError('Location must be a string');
        }
        this._location = value;
    }

    [Symbol.toPrimitive](hint) {
        if (hint === 'number') {
            return this._size;
        }
        if (hint === 'string') {
            return this._location;
        }
        return this._size;
    }
}