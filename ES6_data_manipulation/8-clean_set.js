export default function cleanset(set, startString) {
    if (startString.length === 0) {
        return "";
    }
    const string = [];
    for (const element of set) {
        if (element.startsWith(startString)) {
            string.push(element.slice(startString.length));
        }
    }
    return string.join("-");
}
