export default class Building {
    constructor(sqft) {
        if (new.target !== Building) {
            if (typeof this.evacuationWarningMessage !== 'function') {
                throw new TypeError('Classes extending Building must override evacuationWarningMessage');
            }
        }

        this._sqft = sqft;
    }

    get sqft() {
        return this._sqft;
    }

    set sqft(value) {
        if (typeof value !== 'number') {
            throw new TypeError('Sqft must be a number');
        }
        this._sqft = value;
    }
}
