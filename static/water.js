var world;

var loader;

function setup() {
	
	noCanvas();

	world = new World('VRScene');

	var threeSceneReference = document.querySelector('a-scene').object3D;

	loader = new THREE.MOLLoader();
	loader.load("../static/models/water.mol", (model) => {
		threeSceneReference.add(model);
	});
}

function draw() {

}
