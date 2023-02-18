import torch
model = torch.load('Summarizer')
data = '''The origin of the joints or segments in the limbs of arthropods 
was probably due to the mechanical
strains to which what were at first
soft fleshy outgrowths along the
sides of the body became subjected.
Indeed, certain annelid
worms of the family Syllidæ have
segmented tentacles and parapodia,
as in Dujardinia We do not know enough about the habits of these worms to understand
how this metamerism may have arisen, but it is possibly due
to the act of pushing or repeated efforts to support the body while
creeping over the bottom among broken shells, over coarse gravel,
or among seaweeds.

It is obvious, however, that the jointed structure of the limbs of
arthropods, if we are to attempt any explanation at all of the origin
of such structure, was primarily due mainly to lateral strains and
<span class='pageno' id='Page_35'>35</span>impacts resulting from the primitive endeavors of the ancestral
arthropods to raise and to support the body while thus raised,
and then to push or drag it forward by means of the soft, partially
jointed, lateral limbs which were armed with bristles, hooks, or
finally claws.

On the other hand, by adaptation, or as the result of parasitism and
consequent lack of active motion, the original number of segments
may by disuse be diminished. Thus in adult wasps and bees, the
last three or four abdominal segments may be nearly lost, though the
larval number is ten. During metamorphosis the body is made
over, and the number, shape, and structure of the segments greatly
modified. In the female of the Stylopidæ the thorax loses all traces
of segments, and is fused with the head, and the abdominal segments
are faintly marked, losing their chitin.

While the maxillæ have several joints, the mandibles are 1–jointed,
but there are traces of two joints in Campodea, certain beetles, etc.
In the antenna there is a great elasticity in respect to the number
of joints, which vary from one or two to a hundred or more. It
is likewise so in the thoracic legs, where the number of tarsal joints
varies from one to five; also in the cercopoda, the number of joints
varying from one or two to twelve or more.
'''
answer = model(data,num_sentences=5,min_length=10)
print(answer)