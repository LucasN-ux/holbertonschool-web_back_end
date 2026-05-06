export default function getResponsefromAPI() {
    const promise = new Promise((resolve, reject) => {
        resolve(true);
    });
    promise.then((response) => {
        return response;
    });
    return promise;
}
