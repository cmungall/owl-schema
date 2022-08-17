

CREATE TABLE "AllDifferent" (
	"annotatedProperty" TEXT, 
	"annotatedSource" TEXT, 
	"annotatedTarget" TEXT, 
	members TEXT, 
	"distinctMembers" TEXT, 
	PRIMARY KEY ("annotatedProperty", "annotatedSource", "annotatedTarget", members, "distinctMembers")
);

CREATE TABLE "AllDisjointClasses" (
	"annotatedProperty" TEXT, 
	"annotatedSource" TEXT, 
	"annotatedTarget" TEXT, 
	members TEXT, 
	PRIMARY KEY ("annotatedProperty", "annotatedSource", "annotatedTarget", members)
);

CREATE TABLE "AllDisjointProperties" (
	"annotatedProperty" TEXT, 
	"annotatedSource" TEXT, 
	"annotatedTarget" TEXT, 
	members TEXT, 
	PRIMARY KEY ("annotatedProperty", "annotatedSource", "annotatedTarget", members)
);

CREATE TABLE "Annotation" (
	"annotatedProperty" TEXT, 
	"annotatedSource" TEXT, 
	"annotatedTarget" TEXT, 
	members TEXT, 
	PRIMARY KEY ("annotatedProperty", "annotatedSource", "annotatedTarget", members)
);

CREATE TABLE "AnnotationProperty" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith")
);

CREATE TABLE "AsymmetricProperty" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	"inverseOf" TEXT, 
	"propertyChainAxiom" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith", "inverseOf", "propertyChainAxiom")
);

CREATE TABLE "Axiom" (
	"annotatedProperty" TEXT, 
	"annotatedSource" TEXT, 
	"annotatedTarget" TEXT, 
	members TEXT, 
	PRIMARY KEY ("annotatedProperty", "annotatedSource", "annotatedTarget", members)
);

CREATE TABLE "Class" (
	"complementOf" TEXT, 
	"disjointUnionOf" TEXT, 
	"disjointWith" TEXT, 
	"equivalentClass" TEXT, 
	"hasKey" TEXT, 
	"intersectionOf" TEXT, 
	"oneOf" TEXT, 
	"unionOf" TEXT, 
	PRIMARY KEY ("complementOf", "disjointUnionOf", "disjointWith", "equivalentClass", "hasKey", "intersectionOf", "oneOf", "unionOf")
);

CREATE TABLE "DataRange" (
	"datatypeComplementOf" TEXT, 
	"onDatatype" TEXT, 
	"withRestrictions" TEXT, 
	PRIMARY KEY ("datatypeComplementOf", "onDatatype", "withRestrictions")
);

CREATE TABLE "Datatype" (
	"datatypeComplementOf" TEXT, 
	"onDatatype" TEXT, 
	"withRestrictions" TEXT, 
	PRIMARY KEY ("datatypeComplementOf", "onDatatype", "withRestrictions")
);

CREATE TABLE "DatatypeProperty" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith")
);

CREATE TABLE "DeprecatedClass" (
	"complementOf" TEXT, 
	"disjointUnionOf" TEXT, 
	"disjointWith" TEXT, 
	"equivalentClass" TEXT, 
	"hasKey" TEXT, 
	"intersectionOf" TEXT, 
	"oneOf" TEXT, 
	"unionOf" TEXT, 
	PRIMARY KEY ("complementOf", "disjointUnionOf", "disjointWith", "equivalentClass", "hasKey", "intersectionOf", "oneOf", "unionOf")
);

CREATE TABLE "DeprecatedProperty" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith")
);

CREATE TABLE "FunctionalProperty" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith")
);

CREATE TABLE "InverseFunctionalProperty" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	"inverseOf" TEXT, 
	"propertyChainAxiom" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith", "inverseOf", "propertyChainAxiom")
);

CREATE TABLE "IrreflexiveProperty" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	"inverseOf" TEXT, 
	"propertyChainAxiom" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith", "inverseOf", "propertyChainAxiom")
);

CREATE TABLE "NamedIndividual" (
	"bottomObjectProperty" TEXT, 
	"differentFrom" TEXT, 
	"sameAs" TEXT, 
	"topObjectProperty" TEXT, 
	"bottomDataProperty" TEXT, 
	"topDataProperty" TEXT, 
	PRIMARY KEY ("bottomObjectProperty", "differentFrom", "sameAs", "topObjectProperty", "bottomDataProperty", "topDataProperty")
);

CREATE TABLE "NegativePropertyAssertion" (
	"annotatedProperty" TEXT, 
	"annotatedSource" TEXT, 
	"annotatedTarget" TEXT, 
	members TEXT, 
	"assertionProperty" TEXT, 
	"sourceIndividual" TEXT, 
	"targetIndividual" TEXT, 
	"targetValue" TEXT, 
	PRIMARY KEY ("annotatedProperty", "annotatedSource", "annotatedTarget", members, "assertionProperty", "sourceIndividual", "targetIndividual", "targetValue")
);

CREATE TABLE "Nothing" (
	"bottomObjectProperty" TEXT, 
	"differentFrom" TEXT, 
	"sameAs" TEXT, 
	"topObjectProperty" TEXT, 
	"bottomDataProperty" TEXT, 
	"topDataProperty" TEXT, 
	PRIMARY KEY ("bottomObjectProperty", "differentFrom", "sameAs", "topObjectProperty", "bottomDataProperty", "topDataProperty")
);

CREATE TABLE "ObjectProperty" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	"inverseOf" TEXT, 
	"propertyChainAxiom" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith", "inverseOf", "propertyChainAxiom")
);

CREATE TABLE "Ontology" (
	"annotatedProperty" TEXT, 
	"annotatedSource" TEXT, 
	"annotatedTarget" TEXT, 
	members TEXT, 
	PRIMARY KEY ("annotatedProperty", "annotatedSource", "annotatedTarget", members)
);

CREATE TABLE "OntologyProperty" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith")
);

CREATE TABLE "Property" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith")
);

CREATE TABLE "ReflexiveProperty" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	"inverseOf" TEXT, 
	"propertyChainAxiom" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith", "inverseOf", "propertyChainAxiom")
);

CREATE TABLE "Resource" (
	"annotatedProperty" TEXT, 
	"annotatedSource" TEXT, 
	"annotatedTarget" TEXT, 
	members TEXT, 
	PRIMARY KEY ("annotatedProperty", "annotatedSource", "annotatedTarget", members)
);

CREATE TABLE "Restriction" (
	"complementOf" TEXT, 
	"disjointUnionOf" TEXT, 
	"disjointWith" TEXT, 
	"equivalentClass" TEXT, 
	"hasKey" TEXT, 
	"intersectionOf" TEXT, 
	"oneOf" TEXT, 
	"unionOf" TEXT, 
	"allValuesFrom" TEXT, 
	"hasSelf" TEXT, 
	"hasValue" TEXT, 
	"onClass" TEXT, 
	"onDataRange" TEXT, 
	"onProperties" TEXT, 
	"onProperty" TEXT, 
	"someValuesFrom" TEXT, 
	cardinality TEXT, 
	"maxCardinality" TEXT, 
	"maxQualifiedCardinality" TEXT, 
	"minCardinality" TEXT, 
	"minQualifiedCardinality" TEXT, 
	"qualifiedCardinality" TEXT, 
	PRIMARY KEY ("complementOf", "disjointUnionOf", "disjointWith", "equivalentClass", "hasKey", "intersectionOf", "oneOf", "unionOf", "allValuesFrom", "hasSelf", "hasValue", "onClass", "onDataRange", "onProperties", "onProperty", "someValuesFrom", cardinality, "maxCardinality", "maxQualifiedCardinality", "minCardinality", "minQualifiedCardinality", "qualifiedCardinality")
);

CREATE TABLE "SymmetricProperty" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	"inverseOf" TEXT, 
	"propertyChainAxiom" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith", "inverseOf", "propertyChainAxiom")
);

CREATE TABLE "Thing" (
	"bottomObjectProperty" TEXT, 
	"differentFrom" TEXT, 
	"sameAs" TEXT, 
	"topObjectProperty" TEXT, 
	"bottomDataProperty" TEXT, 
	"topDataProperty" TEXT, 
	PRIMARY KEY ("bottomObjectProperty", "differentFrom", "sameAs", "topObjectProperty", "bottomDataProperty", "topDataProperty")
);

CREATE TABLE "TransitiveProperty" (
	"equivalentProperty" TEXT, 
	"propertyDisjointWith" TEXT, 
	"inverseOf" TEXT, 
	"propertyChainAxiom" TEXT, 
	PRIMARY KEY ("equivalentProperty", "propertyDisjointWith", "inverseOf", "propertyChainAxiom")
);
