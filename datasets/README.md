# Datasets

## Challenge 1

### [challenge-1-Manuscripts-Creators-2024-11-29.csv](./challenge-1-Manuscripts-Creators-2024-11-29.csv)

An export of metadata from the catalogue covering all published Manuscript records. Data was extracted using [Pymarc](https://pymarc.readthedocs.io/en/latest/) and a table generated. Where multiple values were present for a single field they have been concatenated using `;`.

**Rows** - 14,703

The columns are based on the following data:

| column | MARC fields | Description |
| ----- | ----- | ----- |
| mms_id | 001 | Record identifier |
| 037 | 037 | Accession number |
| creator | 100, 110, 111 | Individual or group who created or produced the work. |
| contributor | 700, 710, 711 | Individuals or groups who participated in the creation of the work, with their role. |
| title | 245 | The title assigned to the work. |
| date | 264, 260 | Date the work was produced or published. |
| extent | 300 | Physical description of the item. |
| scope_and_contents | 520 | A description of the material. |
| biographical_note | 545 | A biographical or administrative history of the `creator` |
| copyright | 540, 542* | Used to record Copyright Status for material. May also store other data. |
| 852 MARC | Holdings | Storage location for the material |

More detailed description of MARC fields can be found [MARC 21 format for bibliographic data](https://www.loc.gov/marc/bibliographic/).

Missing fields can be populated using the Alma API Alma: [Alma API documentation](https://developers.exlibrisgroup.com/alma/apis/bibs/)
Or using the source MARC files in `challenge-1-Manuscripts-Full-Records-2024-11-29.mrc` dataset.

### [challenge-1-Manuscripts-Full-Records-2024-11-29.mrc](./challenge-1-Manuscripts-Full-Records-2024-11-29.mrc).

Complete MARC records for Manuscript collection items. Used to produce `challenge-1-Manuscripts-Creators-2024-11-29.csv`.

Can be worked with in Python using [Pymarc](https://pymarc.readthedocs.io/en/latest/)

### [challenge-1-Pictures-Creators-2024-11-29.csv](./challenge-1-Pictures-Creators-2024-11-29.csv)

An export of selected metadata from Alma Analytics for all records in the Pictures Collection, identified by filtering to publicly available records with physical holdings matching `LTAD;PCCARTOON;PCEPHEMERA;PCINF;PCLT;PCLTA;PCLTAEF;PCLTAF;PCLTBOX;PCLTCM;PCLTEFBOX;PCLTFBN;PCLTFBOX;PCLTFURN;PCLTGN;PCLTILLUM;PCLTLS;PCLTM;PCLTPP;PCLTRE;PCLTS;PCLTSL;PCLTST;PCLTTEX;PCLTW;PCLTWEF;PCMCA;PCOVAL;PCPCA;PCPOSTER;PCSILK;PCV;PIC;PICPA;YLTAD;YLTTEX;YPCLT;YPCLTAEF;YPCLTS;YPCPOSTER;YPLTRE`. 

The following filters were applied:

- Remove records with no author recorded
- Remove MANY records

**Rows** - 118,198

#### Column definitions

| Column name | MARC Field(s) | Description |
| ----- | ----- | ----- |
| Author | 100, 110, 111 | Individual or group who created or produced the work. |
| Author (contributor) | 700, 710, 711 | Individuals or groups who participated in the creation of the work, with their role. |
| MMS Id | 001 | Record number in the catalogue system. |
| 037 - Local Param 02 | 037 | State Library Victoria accession number |
| Title (Complete) | 245 a,n,p,h,b,c,f,g,k,s | The title assigned to the work. |
| Publication Date | 264 c, or 260 c, or 008 pos7-10 | Date the work was produced or published. |
| 300 - Local Param 05 | 300 | Physical description of the item. |
| General Note | 500 | Any notes recorded by the cataloguer. |
| 540 - Local Param 09 | 540 | Used to record Terms of use for copyright restrictions. May also store other data. |
| 542 - Local Param 10 | 542 | Used to record Copyright Status for material. May also store other data. |
| Subjects | 6XX excluding 69X, 630, 689 | Topics, themes, people, or formats in the work identified by the cataloguer. |
| Series | 800 t,v, 810 t,v, 811 t,v, 830 a,n,p,v | A title applied to a related group of materials. |
| Location Code | Holdings 852 | Location of the physial item. |

More detail about the meaning of the headings can be found through the Alma Analytics documentation [Physical Items documentation](https://knowledge.exlibrisgroup.com/Alma/Product_Documentation/010Alma_Online_Help_(English)/080Analytics/Alma_Analytics_Subject_Areas/Physical_Items). MARC fields can be checked against [MARC 21 format for bibliographic data](https://www.loc.gov/marc/bibliographic/).

## Challenge 3

### [challenge-3-Image-Pool-2024-11-27](./challenge-3-Image-Pool-2024-11-27.csv)

An export from Rosetta that contains identifiers and metadata for the images that are made available via the "Copyright-free image pool" [https://www.slv.vic.gov.au/images](https://www.slv.vic.gov.au/images).

The `IE PID` column can be used to access the viewer: `https://viewer.slv.vic.gov.au/?entity=<IE_PID>&mode=browse`

API data can be accessed using the `IE_PID` too: `https://viewerapi.slv.vic.gov.au/?entity=<IE_PID>&mode=browse`

The `ALMA _ MMS` can be used to retrieve metadata from Alma using e.g. the API [https://developers.exlibrisgroup.com/alma/apis/bibs/](https://developers.exlibrisgroup.com/alma/apis/bibs/)
