# Auto generated from owl_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-08-16T19:36:07
# Schema: owl
#
# id: http://www.w3.org/2002/07/owl
# description: owl
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'https://w3id.org/None/')
RDF = CurieNamespace('rdf', 'http://example.org/UNKNOWN/rdf/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
DEFAULT_ = OWL


# Types

# Class references



class Literal(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Literal
    class_class_curie: ClassVar[str] = "rdf:Literal"
    class_name: ClassVar[str] = "Literal"
    class_model_uri: ClassVar[URIRef] = OWL.Literal


class List(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.List
    class_class_curie: ClassVar[str] = "rdf:List"
    class_name: ClassVar[str] = "List"
    class_model_uri: ClassVar[URIRef] = OWL.List


@dataclass
class Property(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Property
    class_class_curie: ClassVar[str] = "rdf:Property"
    class_name: ClassVar[str] = "Property"
    class_model_uri: ClassVar[URIRef] = OWL.Property

    equivalentProperty: Optional[Union[Union[dict, "Property"], List[Union[dict, "Property"]]]] = empty_list()
    propertyDisjointWith: Optional[Union[Union[dict, "Property"], List[Union[dict, "Property"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.equivalentProperty, list):
            self.equivalentProperty = [self.equivalentProperty] if self.equivalentProperty is not None else []
        self.equivalentProperty = [v if isinstance(v, Property) else Property(**as_dict(v)) for v in self.equivalentProperty]

        if not isinstance(self.propertyDisjointWith, list):
            self.propertyDisjointWith = [self.propertyDisjointWith] if self.propertyDisjointWith is not None else []
        self.propertyDisjointWith = [v if isinstance(v, Property) else Property(**as_dict(v)) for v in self.propertyDisjointWith]

        super().__post_init__(**kwargs)


class AnnotationProperty(Property):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.AnnotationProperty
    class_class_curie: ClassVar[str] = "owl:AnnotationProperty"
    class_name: ClassVar[str] = "AnnotationProperty"
    class_model_uri: ClassVar[URIRef] = OWL.AnnotationProperty


@dataclass
class Class(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Class
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "Class"
    class_model_uri: ClassVar[URIRef] = OWL.Class

    complementOf: Optional[Union[Union[dict, "Class"], List[Union[dict, "Class"]]]] = empty_list()
    disjointUnionOf: Optional[Union[Union[dict, List], List[Union[dict, List]]]] = empty_list()
    disjointWith: Optional[Union[Union[dict, "Class"], List[Union[dict, "Class"]]]] = empty_list()
    equivalentClass: Optional[Union[Union[dict, "Class"], List[Union[dict, "Class"]]]] = empty_list()
    hasKey: Optional[Union[Union[dict, List], List[Union[dict, List]]]] = empty_list()
    intersectionOf: Optional[Union[Union[dict, List], List[Union[dict, List]]]] = empty_list()
    oneOf: Optional[Union[Union[dict, List], List[Union[dict, List]]]] = empty_list()
    unionOf: Optional[Union[Union[dict, List], List[Union[dict, List]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.complementOf, list):
            self.complementOf = [self.complementOf] if self.complementOf is not None else []
        self.complementOf = [v if isinstance(v, Class) else Class(**as_dict(v)) for v in self.complementOf]

        if not isinstance(self.disjointUnionOf, list):
            self.disjointUnionOf = [self.disjointUnionOf] if self.disjointUnionOf is not None else []
        self.disjointUnionOf = [v if isinstance(v, List) else List(**as_dict(v)) for v in self.disjointUnionOf]

        if not isinstance(self.disjointWith, list):
            self.disjointWith = [self.disjointWith] if self.disjointWith is not None else []
        self.disjointWith = [v if isinstance(v, Class) else Class(**as_dict(v)) for v in self.disjointWith]

        if not isinstance(self.equivalentClass, list):
            self.equivalentClass = [self.equivalentClass] if self.equivalentClass is not None else []
        self.equivalentClass = [v if isinstance(v, Class) else Class(**as_dict(v)) for v in self.equivalentClass]

        if not isinstance(self.hasKey, list):
            self.hasKey = [self.hasKey] if self.hasKey is not None else []
        self.hasKey = [v if isinstance(v, List) else List(**as_dict(v)) for v in self.hasKey]

        if not isinstance(self.intersectionOf, list):
            self.intersectionOf = [self.intersectionOf] if self.intersectionOf is not None else []
        self.intersectionOf = [v if isinstance(v, List) else List(**as_dict(v)) for v in self.intersectionOf]

        if not isinstance(self.oneOf, list):
            self.oneOf = [self.oneOf] if self.oneOf is not None else []
        self.oneOf = [v if isinstance(v, List) else List(**as_dict(v)) for v in self.oneOf]

        if not isinstance(self.unionOf, list):
            self.unionOf = [self.unionOf] if self.unionOf is not None else []
        self.unionOf = [v if isinstance(v, List) else List(**as_dict(v)) for v in self.unionOf]

        super().__post_init__(**kwargs)


class DatatypeProperty(Property):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.DatatypeProperty
    class_class_curie: ClassVar[str] = "owl:DatatypeProperty"
    class_name: ClassVar[str] = "DatatypeProperty"
    class_model_uri: ClassVar[URIRef] = OWL.DatatypeProperty


class DeprecatedClass(Class):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.DeprecatedClass
    class_class_curie: ClassVar[str] = "owl:DeprecatedClass"
    class_name: ClassVar[str] = "DeprecatedClass"
    class_model_uri: ClassVar[URIRef] = OWL.DeprecatedClass


class DeprecatedProperty(Property):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.DeprecatedProperty
    class_class_curie: ClassVar[str] = "owl:DeprecatedProperty"
    class_name: ClassVar[str] = "DeprecatedProperty"
    class_model_uri: ClassVar[URIRef] = OWL.DeprecatedProperty


class FunctionalProperty(Property):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.FunctionalProperty
    class_class_curie: ClassVar[str] = "owl:FunctionalProperty"
    class_name: ClassVar[str] = "FunctionalProperty"
    class_model_uri: ClassVar[URIRef] = OWL.FunctionalProperty


@dataclass
class ObjectProperty(Property):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.ObjectProperty
    class_class_curie: ClassVar[str] = "owl:ObjectProperty"
    class_name: ClassVar[str] = "ObjectProperty"
    class_model_uri: ClassVar[URIRef] = OWL.ObjectProperty

    inverseOf: Optional[Union[Union[dict, "ObjectProperty"], List[Union[dict, "ObjectProperty"]]]] = empty_list()
    propertyChainAxiom: Optional[Union[Union[dict, List], List[Union[dict, List]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.inverseOf, list):
            self.inverseOf = [self.inverseOf] if self.inverseOf is not None else []
        self.inverseOf = [v if isinstance(v, ObjectProperty) else ObjectProperty(**as_dict(v)) for v in self.inverseOf]

        if not isinstance(self.propertyChainAxiom, list):
            self.propertyChainAxiom = [self.propertyChainAxiom] if self.propertyChainAxiom is not None else []
        self.propertyChainAxiom = [v if isinstance(v, List) else List(**as_dict(v)) for v in self.propertyChainAxiom]

        super().__post_init__(**kwargs)


class AsymmetricProperty(ObjectProperty):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.AsymmetricProperty
    class_class_curie: ClassVar[str] = "owl:AsymmetricProperty"
    class_name: ClassVar[str] = "AsymmetricProperty"
    class_model_uri: ClassVar[URIRef] = OWL.AsymmetricProperty


class InverseFunctionalProperty(ObjectProperty):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.InverseFunctionalProperty
    class_class_curie: ClassVar[str] = "owl:InverseFunctionalProperty"
    class_name: ClassVar[str] = "InverseFunctionalProperty"
    class_model_uri: ClassVar[URIRef] = OWL.InverseFunctionalProperty


class IrreflexiveProperty(ObjectProperty):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.IrreflexiveProperty
    class_class_curie: ClassVar[str] = "owl:IrreflexiveProperty"
    class_name: ClassVar[str] = "IrreflexiveProperty"
    class_model_uri: ClassVar[URIRef] = OWL.IrreflexiveProperty


class OntologyProperty(Property):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.OntologyProperty
    class_class_curie: ClassVar[str] = "owl:OntologyProperty"
    class_name: ClassVar[str] = "OntologyProperty"
    class_model_uri: ClassVar[URIRef] = OWL.OntologyProperty


class ReflexiveProperty(ObjectProperty):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.ReflexiveProperty
    class_class_curie: ClassVar[str] = "owl:ReflexiveProperty"
    class_name: ClassVar[str] = "ReflexiveProperty"
    class_model_uri: ClassVar[URIRef] = OWL.ReflexiveProperty


@dataclass
class Restriction(Class):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Restriction
    class_class_curie: ClassVar[str] = "owl:Restriction"
    class_name: ClassVar[str] = "Restriction"
    class_model_uri: ClassVar[URIRef] = OWL.Restriction

    allValuesFrom: Optional[Union[Union[dict, Class], List[Union[dict, Class]]]] = empty_list()
    hasSelf: Optional[Union[Union[dict, "Resource"], List[Union[dict, "Resource"]]]] = empty_list()
    hasValue: Optional[Union[Union[dict, "Resource"], List[Union[dict, "Resource"]]]] = empty_list()
    onClass: Optional[Union[Union[dict, Class], List[Union[dict, Class]]]] = empty_list()
    onDataRange: Optional[Union[Union[dict, "Datatype"], List[Union[dict, "Datatype"]]]] = empty_list()
    onProperties: Optional[Union[Union[dict, List], List[Union[dict, List]]]] = empty_list()
    onProperty: Optional[Union[Union[dict, Property], List[Union[dict, Property]]]] = empty_list()
    someValuesFrom: Optional[Union[Union[dict, Class], List[Union[dict, Class]]]] = empty_list()
    cardinality: Optional[Union[str, List[str]]] = empty_list()
    maxCardinality: Optional[Union[str, List[str]]] = empty_list()
    maxQualifiedCardinality: Optional[Union[str, List[str]]] = empty_list()
    minCardinality: Optional[Union[str, List[str]]] = empty_list()
    minQualifiedCardinality: Optional[Union[str, List[str]]] = empty_list()
    qualifiedCardinality: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.allValuesFrom, list):
            self.allValuesFrom = [self.allValuesFrom] if self.allValuesFrom is not None else []
        self.allValuesFrom = [v if isinstance(v, Class) else Class(**as_dict(v)) for v in self.allValuesFrom]

        if not isinstance(self.hasSelf, list):
            self.hasSelf = [self.hasSelf] if self.hasSelf is not None else []
        self.hasSelf = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.hasSelf]

        if not isinstance(self.hasValue, list):
            self.hasValue = [self.hasValue] if self.hasValue is not None else []
        self.hasValue = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.hasValue]

        if not isinstance(self.onClass, list):
            self.onClass = [self.onClass] if self.onClass is not None else []
        self.onClass = [v if isinstance(v, Class) else Class(**as_dict(v)) for v in self.onClass]

        if not isinstance(self.onDataRange, list):
            self.onDataRange = [self.onDataRange] if self.onDataRange is not None else []
        self.onDataRange = [v if isinstance(v, Datatype) else Datatype(**as_dict(v)) for v in self.onDataRange]

        if not isinstance(self.onProperties, list):
            self.onProperties = [self.onProperties] if self.onProperties is not None else []
        self.onProperties = [v if isinstance(v, List) else List(**as_dict(v)) for v in self.onProperties]

        if not isinstance(self.onProperty, list):
            self.onProperty = [self.onProperty] if self.onProperty is not None else []
        self.onProperty = [v if isinstance(v, Property) else Property(**as_dict(v)) for v in self.onProperty]

        if not isinstance(self.someValuesFrom, list):
            self.someValuesFrom = [self.someValuesFrom] if self.someValuesFrom is not None else []
        self.someValuesFrom = [v if isinstance(v, Class) else Class(**as_dict(v)) for v in self.someValuesFrom]

        if not isinstance(self.cardinality, list):
            self.cardinality = [self.cardinality] if self.cardinality is not None else []
        self.cardinality = [v if isinstance(v, str) else str(v) for v in self.cardinality]

        if not isinstance(self.maxCardinality, list):
            self.maxCardinality = [self.maxCardinality] if self.maxCardinality is not None else []
        self.maxCardinality = [v if isinstance(v, str) else str(v) for v in self.maxCardinality]

        if not isinstance(self.maxQualifiedCardinality, list):
            self.maxQualifiedCardinality = [self.maxQualifiedCardinality] if self.maxQualifiedCardinality is not None else []
        self.maxQualifiedCardinality = [v if isinstance(v, str) else str(v) for v in self.maxQualifiedCardinality]

        if not isinstance(self.minCardinality, list):
            self.minCardinality = [self.minCardinality] if self.minCardinality is not None else []
        self.minCardinality = [v if isinstance(v, str) else str(v) for v in self.minCardinality]

        if not isinstance(self.minQualifiedCardinality, list):
            self.minQualifiedCardinality = [self.minQualifiedCardinality] if self.minQualifiedCardinality is not None else []
        self.minQualifiedCardinality = [v if isinstance(v, str) else str(v) for v in self.minQualifiedCardinality]

        if not isinstance(self.qualifiedCardinality, list):
            self.qualifiedCardinality = [self.qualifiedCardinality] if self.qualifiedCardinality is not None else []
        self.qualifiedCardinality = [v if isinstance(v, str) else str(v) for v in self.qualifiedCardinality]

        super().__post_init__(**kwargs)


class SymmetricProperty(ObjectProperty):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.SymmetricProperty
    class_class_curie: ClassVar[str] = "owl:SymmetricProperty"
    class_name: ClassVar[str] = "SymmetricProperty"
    class_model_uri: ClassVar[URIRef] = OWL.SymmetricProperty


@dataclass
class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Thing
    class_class_curie: ClassVar[str] = "owl:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = OWL.Thing

    bottomObjectProperty: Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]] = empty_list()
    differentFrom: Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]] = empty_list()
    sameAs: Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]] = empty_list()
    topObjectProperty: Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]] = empty_list()
    bottomDataProperty: Optional[Union[str, List[str]]] = empty_list()
    topDataProperty: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.bottomObjectProperty, list):
            self.bottomObjectProperty = [self.bottomObjectProperty] if self.bottomObjectProperty is not None else []
        self.bottomObjectProperty = [v if isinstance(v, Thing) else Thing(**as_dict(v)) for v in self.bottomObjectProperty]

        if not isinstance(self.differentFrom, list):
            self.differentFrom = [self.differentFrom] if self.differentFrom is not None else []
        self.differentFrom = [v if isinstance(v, Thing) else Thing(**as_dict(v)) for v in self.differentFrom]

        if not isinstance(self.sameAs, list):
            self.sameAs = [self.sameAs] if self.sameAs is not None else []
        self.sameAs = [v if isinstance(v, Thing) else Thing(**as_dict(v)) for v in self.sameAs]

        if not isinstance(self.topObjectProperty, list):
            self.topObjectProperty = [self.topObjectProperty] if self.topObjectProperty is not None else []
        self.topObjectProperty = [v if isinstance(v, Thing) else Thing(**as_dict(v)) for v in self.topObjectProperty]

        if not isinstance(self.bottomDataProperty, list):
            self.bottomDataProperty = [self.bottomDataProperty] if self.bottomDataProperty is not None else []
        self.bottomDataProperty = [v if isinstance(v, str) else str(v) for v in self.bottomDataProperty]

        if not isinstance(self.topDataProperty, list):
            self.topDataProperty = [self.topDataProperty] if self.topDataProperty is not None else []
        self.topDataProperty = [v if isinstance(v, str) else str(v) for v in self.topDataProperty]

        super().__post_init__(**kwargs)


class NamedIndividual(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.NamedIndividual
    class_class_curie: ClassVar[str] = "owl:NamedIndividual"
    class_name: ClassVar[str] = "NamedIndividual"
    class_model_uri: ClassVar[URIRef] = OWL.NamedIndividual


class Nothing(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Nothing
    class_class_curie: ClassVar[str] = "owl:Nothing"
    class_name: ClassVar[str] = "Nothing"
    class_model_uri: ClassVar[URIRef] = OWL.Nothing


class TransitiveProperty(ObjectProperty):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.TransitiveProperty
    class_class_curie: ClassVar[str] = "owl:TransitiveProperty"
    class_name: ClassVar[str] = "TransitiveProperty"
    class_model_uri: ClassVar[URIRef] = OWL.TransitiveProperty


@dataclass
class Resource(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Resource
    class_class_curie: ClassVar[str] = "owl:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = OWL.Resource

    annotatedProperty: Optional[Union[Union[dict, "Resource"], List[Union[dict, "Resource"]]]] = empty_list()
    annotatedSource: Optional[Union[Union[dict, "Resource"], List[Union[dict, "Resource"]]]] = empty_list()
    annotatedTarget: Optional[Union[Union[dict, "Resource"], List[Union[dict, "Resource"]]]] = empty_list()
    members: Optional[Union[Union[dict, List], List[Union[dict, List]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.annotatedProperty, list):
            self.annotatedProperty = [self.annotatedProperty] if self.annotatedProperty is not None else []
        self.annotatedProperty = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.annotatedProperty]

        if not isinstance(self.annotatedSource, list):
            self.annotatedSource = [self.annotatedSource] if self.annotatedSource is not None else []
        self.annotatedSource = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.annotatedSource]

        if not isinstance(self.annotatedTarget, list):
            self.annotatedTarget = [self.annotatedTarget] if self.annotatedTarget is not None else []
        self.annotatedTarget = [v if isinstance(v, Resource) else Resource(**as_dict(v)) for v in self.annotatedTarget]

        if not isinstance(self.members, list):
            self.members = [self.members] if self.members is not None else []
        self.members = [v if isinstance(v, List) else List(**as_dict(v)) for v in self.members]

        super().__post_init__(**kwargs)


@dataclass
class AllDifferent(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.AllDifferent
    class_class_curie: ClassVar[str] = "owl:AllDifferent"
    class_name: ClassVar[str] = "AllDifferent"
    class_model_uri: ClassVar[URIRef] = OWL.AllDifferent

    distinctMembers: Optional[Union[Union[dict, List], List[Union[dict, List]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.distinctMembers, list):
            self.distinctMembers = [self.distinctMembers] if self.distinctMembers is not None else []
        self.distinctMembers = [v if isinstance(v, List) else List(**as_dict(v)) for v in self.distinctMembers]

        super().__post_init__(**kwargs)


class AllDisjointClasses(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.AllDisjointClasses
    class_class_curie: ClassVar[str] = "owl:AllDisjointClasses"
    class_name: ClassVar[str] = "AllDisjointClasses"
    class_model_uri: ClassVar[URIRef] = OWL.AllDisjointClasses


class AllDisjointProperties(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.AllDisjointProperties
    class_class_curie: ClassVar[str] = "owl:AllDisjointProperties"
    class_name: ClassVar[str] = "AllDisjointProperties"
    class_model_uri: ClassVar[URIRef] = OWL.AllDisjointProperties


class Annotation(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Annotation
    class_class_curie: ClassVar[str] = "owl:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = OWL.Annotation


class Axiom(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Axiom
    class_class_curie: ClassVar[str] = "owl:Axiom"
    class_name: ClassVar[str] = "Axiom"
    class_model_uri: ClassVar[URIRef] = OWL.Axiom


@dataclass
class NegativePropertyAssertion(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.NegativePropertyAssertion
    class_class_curie: ClassVar[str] = "owl:NegativePropertyAssertion"
    class_name: ClassVar[str] = "NegativePropertyAssertion"
    class_model_uri: ClassVar[URIRef] = OWL.NegativePropertyAssertion

    assertionProperty: Optional[Union[Union[dict, Property], List[Union[dict, Property]]]] = empty_list()
    sourceIndividual: Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]] = empty_list()
    targetIndividual: Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]] = empty_list()
    targetValue: Optional[Union[Union[dict, Literal], List[Union[dict, Literal]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.assertionProperty, list):
            self.assertionProperty = [self.assertionProperty] if self.assertionProperty is not None else []
        self.assertionProperty = [v if isinstance(v, Property) else Property(**as_dict(v)) for v in self.assertionProperty]

        if not isinstance(self.sourceIndividual, list):
            self.sourceIndividual = [self.sourceIndividual] if self.sourceIndividual is not None else []
        self.sourceIndividual = [v if isinstance(v, Thing) else Thing(**as_dict(v)) for v in self.sourceIndividual]

        if not isinstance(self.targetIndividual, list):
            self.targetIndividual = [self.targetIndividual] if self.targetIndividual is not None else []
        self.targetIndividual = [v if isinstance(v, Thing) else Thing(**as_dict(v)) for v in self.targetIndividual]

        if not isinstance(self.targetValue, list):
            self.targetValue = [self.targetValue] if self.targetValue is not None else []
        self.targetValue = [v if isinstance(v, Literal) else Literal(**as_dict(v)) for v in self.targetValue]

        super().__post_init__(**kwargs)


class Ontology(Resource):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Ontology
    class_class_curie: ClassVar[str] = "owl:Ontology"
    class_name: ClassVar[str] = "Ontology"
    class_model_uri: ClassVar[URIRef] = OWL.Ontology


@dataclass
class Datatype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Datatype
    class_class_curie: ClassVar[str] = "owl:Datatype"
    class_name: ClassVar[str] = "Datatype"
    class_model_uri: ClassVar[URIRef] = OWL.Datatype

    datatypeComplementOf: Optional[Union[Union[dict, "Datatype"], List[Union[dict, "Datatype"]]]] = empty_list()
    onDatatype: Optional[Union[Union[dict, "Datatype"], List[Union[dict, "Datatype"]]]] = empty_list()
    withRestrictions: Optional[Union[Union[dict, List], List[Union[dict, List]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.datatypeComplementOf, list):
            self.datatypeComplementOf = [self.datatypeComplementOf] if self.datatypeComplementOf is not None else []
        self.datatypeComplementOf = [v if isinstance(v, Datatype) else Datatype(**as_dict(v)) for v in self.datatypeComplementOf]

        if not isinstance(self.onDatatype, list):
            self.onDatatype = [self.onDatatype] if self.onDatatype is not None else []
        self.onDatatype = [v if isinstance(v, Datatype) else Datatype(**as_dict(v)) for v in self.onDatatype]

        if not isinstance(self.withRestrictions, list):
            self.withRestrictions = [self.withRestrictions] if self.withRestrictions is not None else []
        self.withRestrictions = [v if isinstance(v, List) else List(**as_dict(v)) for v in self.withRestrictions]

        super().__post_init__(**kwargs)


class DataRange(Datatype):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.DataRange
    class_class_curie: ClassVar[str] = "owl:DataRange"
    class_name: ClassVar[str] = "DataRange"
    class_model_uri: ClassVar[URIRef] = OWL.DataRange


# Enumerations


# Slots
class slots:
    pass

slots.domain = Slot(uri=RDFS.domain, name="domain", curie=RDFS.curie('domain'),
                   model_uri=OWL.domain, domain=None, range=Optional[Union[str, List[str]]])

slots.member = Slot(uri=RDFS.member, name="member", curie=RDFS.curie('member'),
                   model_uri=OWL.member, domain=None, range=Optional[Union[str, List[str]]])

slots.range = Slot(uri=RDFS.range, name="range", curie=RDFS.curie('range'),
                   model_uri=OWL.range, domain=None, range=Optional[Union[str, List[str]]])

slots.subClassOf = Slot(uri=RDFS.subClassOf, name="subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=OWL.subClassOf, domain=None, range=Optional[Union[str, List[str]]])

slots.subPropertyOf = Slot(uri=RDFS.subPropertyOf, name="subPropertyOf", curie=RDFS.curie('subPropertyOf'),
                   model_uri=OWL.subPropertyOf, domain=None, range=Optional[Union[str, List[str]]])

slots.allValuesFrom = Slot(uri=OWL.allValuesFrom, name="allValuesFrom", curie=OWL.curie('allValuesFrom'),
                   model_uri=OWL.allValuesFrom, domain=None, range=Optional[Union[Union[dict, Class], List[Union[dict, Class]]]])

slots.annotatedProperty = Slot(uri=OWL.annotatedProperty, name="annotatedProperty", curie=OWL.curie('annotatedProperty'),
                   model_uri=OWL.annotatedProperty, domain=None, range=Optional[Union[Union[dict, Resource], List[Union[dict, Resource]]]])

slots.annotatedSource = Slot(uri=OWL.annotatedSource, name="annotatedSource", curie=OWL.curie('annotatedSource'),
                   model_uri=OWL.annotatedSource, domain=None, range=Optional[Union[Union[dict, Resource], List[Union[dict, Resource]]]])

slots.annotatedTarget = Slot(uri=OWL.annotatedTarget, name="annotatedTarget", curie=OWL.curie('annotatedTarget'),
                   model_uri=OWL.annotatedTarget, domain=None, range=Optional[Union[Union[dict, Resource], List[Union[dict, Resource]]]])

slots.assertionProperty = Slot(uri=OWL.assertionProperty, name="assertionProperty", curie=OWL.curie('assertionProperty'),
                   model_uri=OWL.assertionProperty, domain=None, range=Optional[Union[Union[dict, Property], List[Union[dict, Property]]]])

slots.bottomObjectProperty = Slot(uri=OWL.bottomObjectProperty, name="bottomObjectProperty", curie=OWL.curie('bottomObjectProperty'),
                   model_uri=OWL.bottomObjectProperty, domain=None, range=Optional[Union[Union[dict, Thing], List[Union[dict, Thing]]]])

slots.complementOf = Slot(uri=OWL.complementOf, name="complementOf", curie=OWL.curie('complementOf'),
                   model_uri=OWL.complementOf, domain=None, range=Optional[Union[Union[dict, Class], List[Union[dict, Class]]]])

slots.datatypeComplementOf = Slot(uri=OWL.datatypeComplementOf, name="datatypeComplementOf", curie=OWL.curie('datatypeComplementOf'),
                   model_uri=OWL.datatypeComplementOf, domain=None, range=Optional[Union[Union[dict, Datatype], List[Union[dict, Datatype]]]])

slots.differentFrom = Slot(uri=OWL.differentFrom, name="differentFrom", curie=OWL.curie('differentFrom'),
                   model_uri=OWL.differentFrom, domain=None, range=Optional[Union[Union[dict, Thing], List[Union[dict, Thing]]]])

slots.disjointUnionOf = Slot(uri=OWL.disjointUnionOf, name="disjointUnionOf", curie=OWL.curie('disjointUnionOf'),
                   model_uri=OWL.disjointUnionOf, domain=None, range=Optional[Union[Union[dict, List], List[Union[dict, List]]]])

slots.disjointWith = Slot(uri=OWL.disjointWith, name="disjointWith", curie=OWL.curie('disjointWith'),
                   model_uri=OWL.disjointWith, domain=None, range=Optional[Union[Union[dict, Class], List[Union[dict, Class]]]])

slots.distinctMembers = Slot(uri=OWL.distinctMembers, name="distinctMembers", curie=OWL.curie('distinctMembers'),
                   model_uri=OWL.distinctMembers, domain=None, range=Optional[Union[Union[dict, List], List[Union[dict, List]]]])

slots.equivalentClass = Slot(uri=OWL.equivalentClass, name="equivalentClass", curie=OWL.curie('equivalentClass'),
                   model_uri=OWL.equivalentClass, domain=None, range=Optional[Union[Union[dict, Class], List[Union[dict, Class]]]])

slots.equivalentProperty = Slot(uri=OWL.equivalentProperty, name="equivalentProperty", curie=OWL.curie('equivalentProperty'),
                   model_uri=OWL.equivalentProperty, domain=None, range=Optional[Union[Union[dict, Property], List[Union[dict, Property]]]])

slots.hasKey = Slot(uri=OWL.hasKey, name="hasKey", curie=OWL.curie('hasKey'),
                   model_uri=OWL.hasKey, domain=None, range=Optional[Union[Union[dict, List], List[Union[dict, List]]]])

slots.hasSelf = Slot(uri=OWL.hasSelf, name="hasSelf", curie=OWL.curie('hasSelf'),
                   model_uri=OWL.hasSelf, domain=None, range=Optional[Union[Union[dict, Resource], List[Union[dict, Resource]]]])

slots.hasValue = Slot(uri=OWL.hasValue, name="hasValue", curie=OWL.curie('hasValue'),
                   model_uri=OWL.hasValue, domain=None, range=Optional[Union[Union[dict, Resource], List[Union[dict, Resource]]]])

slots.intersectionOf = Slot(uri=OWL.intersectionOf, name="intersectionOf", curie=OWL.curie('intersectionOf'),
                   model_uri=OWL.intersectionOf, domain=None, range=Optional[Union[Union[dict, List], List[Union[dict, List]]]])

slots.inverseOf = Slot(uri=OWL.inverseOf, name="inverseOf", curie=OWL.curie('inverseOf'),
                   model_uri=OWL.inverseOf, domain=None, range=Optional[Union[Union[dict, ObjectProperty], List[Union[dict, ObjectProperty]]]])

slots.members = Slot(uri=OWL.members, name="members", curie=OWL.curie('members'),
                   model_uri=OWL.members, domain=None, range=Optional[Union[Union[dict, List], List[Union[dict, List]]]])

slots.onClass = Slot(uri=OWL.onClass, name="onClass", curie=OWL.curie('onClass'),
                   model_uri=OWL.onClass, domain=None, range=Optional[Union[Union[dict, Class], List[Union[dict, Class]]]])

slots.onDataRange = Slot(uri=OWL.onDataRange, name="onDataRange", curie=OWL.curie('onDataRange'),
                   model_uri=OWL.onDataRange, domain=None, range=Optional[Union[Union[dict, Datatype], List[Union[dict, Datatype]]]])

slots.onDatatype = Slot(uri=OWL.onDatatype, name="onDatatype", curie=OWL.curie('onDatatype'),
                   model_uri=OWL.onDatatype, domain=None, range=Optional[Union[Union[dict, Datatype], List[Union[dict, Datatype]]]])

slots.onProperties = Slot(uri=OWL.onProperties, name="onProperties", curie=OWL.curie('onProperties'),
                   model_uri=OWL.onProperties, domain=None, range=Optional[Union[Union[dict, List], List[Union[dict, List]]]])

slots.onProperty = Slot(uri=OWL.onProperty, name="onProperty", curie=OWL.curie('onProperty'),
                   model_uri=OWL.onProperty, domain=None, range=Optional[Union[Union[dict, Property], List[Union[dict, Property]]]])

slots.oneOf = Slot(uri=OWL.oneOf, name="oneOf", curie=OWL.curie('oneOf'),
                   model_uri=OWL.oneOf, domain=None, range=Optional[Union[Union[dict, List], List[Union[dict, List]]]])

slots.propertyChainAxiom = Slot(uri=OWL.propertyChainAxiom, name="propertyChainAxiom", curie=OWL.curie('propertyChainAxiom'),
                   model_uri=OWL.propertyChainAxiom, domain=None, range=Optional[Union[Union[dict, List], List[Union[dict, List]]]])

slots.propertyDisjointWith = Slot(uri=OWL.propertyDisjointWith, name="propertyDisjointWith", curie=OWL.curie('propertyDisjointWith'),
                   model_uri=OWL.propertyDisjointWith, domain=None, range=Optional[Union[Union[dict, Property], List[Union[dict, Property]]]])

slots.sameAs = Slot(uri=OWL.sameAs, name="sameAs", curie=OWL.curie('sameAs'),
                   model_uri=OWL.sameAs, domain=None, range=Optional[Union[Union[dict, Thing], List[Union[dict, Thing]]]])

slots.someValuesFrom = Slot(uri=OWL.someValuesFrom, name="someValuesFrom", curie=OWL.curie('someValuesFrom'),
                   model_uri=OWL.someValuesFrom, domain=None, range=Optional[Union[Union[dict, Class], List[Union[dict, Class]]]])

slots.sourceIndividual = Slot(uri=OWL.sourceIndividual, name="sourceIndividual", curie=OWL.curie('sourceIndividual'),
                   model_uri=OWL.sourceIndividual, domain=None, range=Optional[Union[Union[dict, Thing], List[Union[dict, Thing]]]])

slots.targetIndividual = Slot(uri=OWL.targetIndividual, name="targetIndividual", curie=OWL.curie('targetIndividual'),
                   model_uri=OWL.targetIndividual, domain=None, range=Optional[Union[Union[dict, Thing], List[Union[dict, Thing]]]])

slots.targetValue = Slot(uri=OWL.targetValue, name="targetValue", curie=OWL.curie('targetValue'),
                   model_uri=OWL.targetValue, domain=None, range=Optional[Union[Union[dict, Literal], List[Union[dict, Literal]]]])

slots.topObjectProperty = Slot(uri=OWL.topObjectProperty, name="topObjectProperty", curie=OWL.curie('topObjectProperty'),
                   model_uri=OWL.topObjectProperty, domain=None, range=Optional[Union[Union[dict, Thing], List[Union[dict, Thing]]]])

slots.unionOf = Slot(uri=OWL.unionOf, name="unionOf", curie=OWL.curie('unionOf'),
                   model_uri=OWL.unionOf, domain=None, range=Optional[Union[Union[dict, List], List[Union[dict, List]]]])

slots.withRestrictions = Slot(uri=OWL.withRestrictions, name="withRestrictions", curie=OWL.curie('withRestrictions'),
                   model_uri=OWL.withRestrictions, domain=None, range=Optional[Union[Union[dict, List], List[Union[dict, List]]]])

slots.bottomDataProperty = Slot(uri=OWL.bottomDataProperty, name="bottomDataProperty", curie=OWL.curie('bottomDataProperty'),
                   model_uri=OWL.bottomDataProperty, domain=None, range=Optional[Union[str, List[str]]])

slots.cardinality = Slot(uri=OWL.cardinality, name="cardinality", curie=OWL.curie('cardinality'),
                   model_uri=OWL.cardinality, domain=None, range=Optional[Union[str, List[str]]])

slots.maxCardinality = Slot(uri=OWL.maxCardinality, name="maxCardinality", curie=OWL.curie('maxCardinality'),
                   model_uri=OWL.maxCardinality, domain=None, range=Optional[Union[str, List[str]]])

slots.maxQualifiedCardinality = Slot(uri=OWL.maxQualifiedCardinality, name="maxQualifiedCardinality", curie=OWL.curie('maxQualifiedCardinality'),
                   model_uri=OWL.maxQualifiedCardinality, domain=None, range=Optional[Union[str, List[str]]])

slots.minCardinality = Slot(uri=OWL.minCardinality, name="minCardinality", curie=OWL.curie('minCardinality'),
                   model_uri=OWL.minCardinality, domain=None, range=Optional[Union[str, List[str]]])

slots.minQualifiedCardinality = Slot(uri=OWL.minQualifiedCardinality, name="minQualifiedCardinality", curie=OWL.curie('minQualifiedCardinality'),
                   model_uri=OWL.minQualifiedCardinality, domain=None, range=Optional[Union[str, List[str]]])

slots.qualifiedCardinality = Slot(uri=OWL.qualifiedCardinality, name="qualifiedCardinality", curie=OWL.curie('qualifiedCardinality'),
                   model_uri=OWL.qualifiedCardinality, domain=None, range=Optional[Union[str, List[str]]])

slots.topDataProperty = Slot(uri=OWL.topDataProperty, name="topDataProperty", curie=OWL.curie('topDataProperty'),
                   model_uri=OWL.topDataProperty, domain=None, range=Optional[Union[str, List[str]]])

slots.title = Slot(uri="str(uriorcurie)", name="title", curie=None,
                   model_uri=OWL.title, domain=None, range=Optional[Union[str, List[str]]])

slots.backwardCompatibleWith = Slot(uri=OWL.backwardCompatibleWith, name="backwardCompatibleWith", curie=OWL.curie('backwardCompatibleWith'),
                   model_uri=OWL.backwardCompatibleWith, domain=None, range=Optional[Union[Union[dict, Ontology], List[Union[dict, Ontology]]]])

slots.deprecated = Slot(uri=OWL.deprecated, name="deprecated", curie=OWL.curie('deprecated'),
                   model_uri=OWL.deprecated, domain=None, range=Optional[Union[Union[dict, Resource], List[Union[dict, Resource]]]])

slots.imports = Slot(uri=OWL.imports, name="imports", curie=OWL.curie('imports'),
                   model_uri=OWL.imports, domain=None, range=Optional[Union[Union[dict, Ontology], List[Union[dict, Ontology]]]])

slots.incompatibleWith = Slot(uri=OWL.incompatibleWith, name="incompatibleWith", curie=OWL.curie('incompatibleWith'),
                   model_uri=OWL.incompatibleWith, domain=None, range=Optional[Union[Union[dict, Ontology], List[Union[dict, Ontology]]]])

slots.priorVersion = Slot(uri=OWL.priorVersion, name="priorVersion", curie=OWL.curie('priorVersion'),
                   model_uri=OWL.priorVersion, domain=None, range=Optional[Union[Union[dict, Ontology], List[Union[dict, Ontology]]]])

slots.versionIRI = Slot(uri=OWL.versionIRI, name="versionIRI", curie=OWL.curie('versionIRI'),
                   model_uri=OWL.versionIRI, domain=None, range=Optional[Union[Union[dict, Ontology], List[Union[dict, Ontology]]]])

slots.versionInfo = Slot(uri=OWL.versionInfo, name="versionInfo", curie=OWL.curie('versionInfo'),
                   model_uri=OWL.versionInfo, domain=None, range=Optional[Union[Union[dict, Resource], List[Union[dict, Resource]]]])

slots.namespaceTransformation = Slot(uri="str(uriorcurie)", name="namespaceTransformation", curie=None,
                   model_uri=OWL.namespaceTransformation, domain=None, range=Optional[Union[str, List[str]]])