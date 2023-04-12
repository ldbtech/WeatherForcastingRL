// Initialize Three.js
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );
var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

// Add plane to the scene
var planeGeometry = new THREE.PlaneGeometry( 50, 50 );
var planeMaterial = new THREE.MeshBasicMaterial( {color: 0xffffff, side: THREE.DoubleSide} );
var plane = new THREE.Mesh( planeGeometry, planeMaterial );
plane.rotation.x = -Math.PI/2;
scene.add( plane );

// Add runway to the scene
var runwayGeometry = new THREE.BoxGeometry( 50, 0.1, 5 );
var runwayMaterial = new THREE.MeshBasicMaterial( {color: 0xff0000} );
var runway = new THREE.Mesh( runwayGeometry, runwayMaterial );
runway.position.z = -20;
scene.add( runway );

// Add control tower to the scene
var towerGeometry = new THREE.BoxGeometry( 5, 20, 5 );
var towerMaterial = new THREE.MeshBasicMaterial( {color: 0x00ff00} );
var tower = new THREE.Mesh( towerGeometry, towerMaterial );
tower.position.x = 20;
scene.add( tower );

// Add ambient light to the scene
var ambientLight = new THREE.AmbientLight( 0xffffff, 0.5 );
scene.add( ambientLight );

// Add directional light to the scene
var directionalLight = new THREE.DirectionalLight( 0xffffff, 0.5 );
directionalLight.position.set( 1, 1, 1 );
scene.add( directionalLight );

// Update the camera position
camera.position.z = 30;

// Render the scene
var animate = function () {
    requestAnimationFrame( animate );

    // Rotate the runway
    runway.rotation.x += 0.01;

    renderer.render( scene, camera );
};

animate();
