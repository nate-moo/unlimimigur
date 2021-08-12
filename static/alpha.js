// Helper functions:
function randomNumber(min, max) { 
    return Math.floor(Math.random() * (max - min) + min);
} 





// listen for `onload` event
// xhr.onload = () => {
//     // statusCode = 0;
//     if (xhr.status == 200) {
//         console.log('Image exists.');
//         // localStorage.setItem('statusCode', `${xhr.status}`);
//         // statusCode = 200;
//     } else {
//         console.log('Image does not exist.');
//         // statusCode = xhr.status;
//     }
    
// };

// xhr.onerror = () => {
//     console.log('Image does not exist.');
//     // statusCode = xhr.status;
// }

function testImage(url, callback, timeout) {
    timeout = timeout || 5000;
    var timedOut = false, timer;
    var img = new Image();
    img.onerror = img.onabort = function() {
        if (!timedOut) {
            clearTimeout(timer);
            callback(url, "error");
        }
    };
    img.onload = function() {
        if (!timedOut) {
            clearTimeout(timer);
            callback(url, "success");
        }
    };
    img.src = url;
    timer = setTimeout(function() {
        timedOut = true;
        callback(url, "timeout");
    }, timeout); 
}

// Main generation function:
async function GenerateID() {
    // create an XHR object
    const xhr = new XMLHttpRequest(); 
    // var statusCode = 0;
    // A string with letters
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890";
    let returnVar = "";
    let randStr = "";
    for (let step = 0; step < 6; step++) {
        randStr += letters[randomNumber(0, 62)];
    }

    const link = "https://i.imgur.com/" + randStr + ".jpeg";

    // imgurImage = new Image();
    // img.onload

    // const res = await fetch(link, { method: "HEAD", mode: "no-cors" });

    // if (!res.redirected) {
    //     return res.url;
    // } else {
    // }

    xhr.open('HEAD', link);

    // // let statusCode = 302;

    // // try {
    xhr.send();

    let statusCode = 0;

    // console.log(xhr.status);

    // return link;

    xhr.onload = function (resolve, reject) {
        if (xhr.status == 200) {
            statusCode = 200;
            // resolve(xhr.status);
        } else {
            statusCode = 0;
            // reject(xhr.status);
        }
    }

    xhr.onerror = function () {
        // statusCode = xhr.status;
        // console.log(xhr.status);
        statusCode = 0;
    } 


    
    // //     // statusCode = 200;
    // // // } catch (error) {
    // //     // statusCode = 302;
    // // // }

    if (statusCode === 200) {
        console.log(statusCode);
        console.log(link);
        return link;
    } else {
        return "Fuck you"
    }
        

}