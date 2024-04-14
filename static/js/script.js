let scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000); // Устанавливаем черный цвет фона
scene.background.a = 0; // Устанавливаем прозрачность фона

let camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 0, 13);

// Затем отрицательно сместите все объекты в сцене
scene.traverse(function (object) {
    if (object instanceof THREE.Mesh) {
        object.position.sub(centerPoint);
    }
});

let renderer = new THREE.WebGLRenderer({alpha: true, antialias: true});
renderer.setClearColor(0x000000, 0);
updateRendererSize(); // Устанавливаем размер рендерера в соответствии с размером окна
function updateRendererSize() {
    renderer.setSize(window.innerWidth, window.innerHeight);
}
window.addEventListener('resize', function() {
    updateRendererSize(); // Обновляем размер рендерера при изменении размера окна
});


renderer.domElement.setAttribute("id", "TwitPlex3DObj");
document.body.insertBefore(renderer.domElement, document.body.firstChild);

let aLight = new THREE.AmbientLight(0x404040, 1.2);
scene.add(aLight);

let pLight = new THREE.PointLight(0xFFFFFF, 3.2);
pLight.position.set(-10, 5, -10);
scene.add(pLight);

let pLight2 = new THREE.PointLight(0xFFFFFF, 2.2);
pLight2.position.set(-10, 5, 10);
scene.add(pLight2);

let pLight3 = new THREE.PointLight(0xFFFFFF, 3.2);
pLight3.position.set(10, 5, 10);
scene.add(pLight3);

let pLight4 = new THREE.PointLight(0x47b5ed, 1.2);
pLight4.position.set(0, -10, 0);
scene.add(pLight4);

let pLight5 = new THREE.PointLight(0x47b5ed, 1.2);
pLight5.position.set(0, 10, 0);
scene.add(pLight5);

let loader = new THREE.GLTFLoader();
const degrees = 15; // Угол в градусах
const radians = degrees * Math.PI / 180; // Конвертация градусов в радианы
const degrees2 = -10; // Угол в градусах
const radians2 = degrees2 * Math.PI / 180; // Конвертация градусов в радианы



let model; // Сохраняем модель в переменной, чтобы обращаться к ней в функции animate()

loader.load(url, function(gltf) {
    gltf.scene.scale.set(0.3, 0.3, 0.3);
    gltf.scene.rotation.y = degrees2; // Применение начального поворота
    gltf.scene.position.x = 4;
    gltf.scene.position.y = -0.5;
    scene.add(gltf.scene);
    model = gltf.scene; // Сохраняем модель

    if (gltf.animations && gltf.animations.length > 0) { // Проверяем наличие анимаций
        mixer = new THREE.AnimationMixer(gltf.scene);
        let action = mixer.clipAction(gltf.animations[0]);
        action.play();
    }
    
    const el = document.getElementById('TwitPlex3DObj');
    el.classList.add('animate__animated', 'animate__delay-2s', 'animate__fadeInUp');
    animate(); // Запускаем анимацию после загрузки модели
});

let endRotation = radians; // Установите конечный угол вращения в противоположном направлении
let currentRotation = 0; // Сохраняем текущее значение угла вращения
let time = 1; // Время для плавного перехода

function animate() {
    requestAnimationFrame(animate);

    // Увеличиваем время
    time += 0.006;

    // Используем синусоиду для плавного перехода между начальным и конечным углами
    let smoothRotation = radians2 + (radians - radians2) * Math.sin(time);

    // Вращаем модель каждый кадр
    if (model) {
        model.rotation.y = smoothRotation;
    }
    if (model) {
        model.rotation.z = smoothRotation;
    }
    renderer.render(scene, camera);
}

let clock = new THREE.Clock();