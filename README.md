# ![freeLogo](https://user-images.githubusercontent.com/49564849/68621524-05391080-04e1-11ea-907f-c0314c61416f.jpeg)

MOL.VR(Beta) - is an open source tool designed to search for information about a substance in the database using the camera of your phone or tablet.
 
### INTRODUCE

Experience in the construction of molecular graphs shows that the most accurate are the questions of accurately determining the coordinates of a vertex molecule.
At the moment, work is underway on the accuracy of determining SMILES, and the accuracy of rendering, determining vertices and nodes.
There are several possible solutions you can use:
1) Machine learning.
2) Pre-processing of photos and pictures for a more accurate result (our option).
3) Finalize the solution with the addition of the library and try to process the existing database with it.
Each individual approach does not always show the best result, the solution is often incomplete and / or inaccurate. An important role is played by the quality of the processed image.
The existing solutions are separate disparate algorithms and toolkits for recognizing 2D images of a chemical.

```
EXAMPLE

var smiles=get('smiles').split(/[\r\n\t ;,]+/).filter(s => s);

var results=smiles.map( smile => {
    var molecule=OCL.Molecule.fromSmiles(smile);
    var mf=molecule.getMolecularFormula();
    var properties=new OCL.MoleculeProperties(molecule);
    
    return {
        smiles: smile,
        mw:mf.relativeWeight,
        em:mf.absoluteWeight,
        mf:mf.formula,
        logP: properties.logP,
        logS: properties.logS,
        psa: properties.polarSurfaceArea
    }
    
})

API.createData('results', results);

```


### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Built With

* [Python](https://www.python.org/)
* [JavaScript](https://www.javascript.com/)
* [FLASK](https://www.palletsprojects.com/p/flask/)
* [Imago](https://lifescience.opensource.epam.com/imago/imago_console.html)


## Authors

* **Dobroklonskaya M.** - ** - [](https://github.com/PurpleBooth)
* **Chaplygin A.** - ** - [](https://github.com/PurpleBooth)
* **Mayorov U.** - ** - [](https://github.com/PurpleBooth)
* **Korotkov S.** - ** - [therealadespina](https://github.com/therealadespina)
* **Koryakovsky D.** - ** - [](https://github.com/PurpleBooth)
