function distanceBetweenPoints(arr)
{
    let x1 = Number(arr[0]);
    let y1 = Number(arr[1]);
    let x2 = Number(arr[2]);
    let y2 = Number(arr[3]);
    let point1 = {x: x1, y: y1};
    let point2 = {x: x2, y: y2};
    let distance = Math.sqrt(Math.pow(point1.x - point2.x, 2) + Math.pow(point1.y - point2.y, 2));
    console.log(distance);
}
let arr = ['2', '4', '5', '0'];
distanceBetweenPoints(arr);