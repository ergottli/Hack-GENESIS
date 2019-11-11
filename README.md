# ![freeLogo](https://user-images.githubusercontent.com/49564849/68621524-05391080-04e1-11ea-907f-c0314c61416f.jpeg)

MOL.VR(Beta) - is an open source tool designed to search for information about a substance in the database using the camera of your phone or tablet.
 
## INTRODUCE

Experience in the construction of molecular graphs shows that the most accurate are the questions of accurately determining the coordinates of a vertex molecule. Each individual approach does not always show the best result, the solution is often incomplete and / or inaccurate. The existing solutions are separate disparate algorithms and toolkits for recognizing 2D images of a chemical.
At the moment, work is underway on the accuracy of determining SMILES, and the accuracy of rendering, determining vertices and nodes.
There are several possible solutions we can use:
1) Machine learning.
2) Pre-processing of photos and pictures for a more accurate result (our option). An important role is played by the quality of the processed image.
3) Finalize the solution with the addition of the library and try to process the existing database with it.

```
EXAMPLE(SMILES)

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
An example is shown above, but it works, this is not the end result of the product.

## Built With

* [Python](https://www.python.org/)
* [JavaScript](https://www.javascript.com/)
* [FLASK](https://www.palletsprojects.com/p/flask/)
* [Imago](https://lifescience.opensource.epam.com/imago/imago_console.html)


## Authors

* **Dobroklonskaya M.**  - [marina](https://github.com/marina1177)
* **Chaplygin A.** - ** - [ergottli](https://github.com/ergottli)
* **Mayorov U.** - ** - [noreederek](https://github.com/noreederek)
* **Korotkov S.** - ** - [therealadespina](https://github.com/therealadespina)
* **Koryakovsky D.**
