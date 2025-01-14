
//------------------------------------------------------------------------------
// This code was generated by a tool.
//
//   Tool : Bond Compiler 0.12.1.0
//   Input filename:  benchmark/commitlint/bond/schema.bond
//   Output filename: schema_reflection.h
//
// Changes to this file may cause incorrect behavior and will be lost when
// the code is regenerated.
// <auto-generated />
//------------------------------------------------------------------------------

#pragma once

#include "schema_types.h"
#include <bond/core/reflection.h>

namespace benchmark
{
    //
    // Rule
    //
    struct Rule::Schema
    {
        typedef ::bond::no_base base;

        static const ::bond::Metadata metadata;
        
        private: static const ::bond::Metadata s_textual_metadata;
        private: static const ::bond::Metadata s_numeric_metadata;
        private: static const ::bond::Metadata s_multitextual_metadata;

        public: struct var
        {
            // textual
            typedef struct textual_type : ::bond::reflection::FieldTemplate<
                0,
                ::bond::reflection::optional_field_modifier,
                Rule,
                ::bond::maybe<std::string>,
                &Rule::textual,
                &s_textual_metadata
            > {} textual;
        
            // numeric
            typedef struct numeric_type : ::bond::reflection::FieldTemplate<
                1,
                ::bond::reflection::optional_field_modifier,
                Rule,
                ::bond::maybe<uint8_t>,
                &Rule::numeric,
                &s_numeric_metadata
            > {} numeric;
        
            // multitextual
            typedef struct multitextual_type : ::bond::reflection::FieldTemplate<
                2,
                ::bond::reflection::optional_field_modifier,
                Rule,
                ::bond::maybe<std::list<std::string> >,
                &Rule::multitextual,
                &s_multitextual_metadata
            > {} multitextual;
        };

        private: typedef boost::mpl::list<> fields0;
        private: typedef boost::mpl::push_front<fields0, var::multitextual>::type fields1;
        private: typedef boost::mpl::push_front<fields1, var::numeric>::type fields2;
        private: typedef boost::mpl::push_front<fields2, var::textual>::type fields3;

        public: typedef fields3::type fields;
        
        
        static ::bond::Metadata GetMetadata()
        {
            return ::bond::reflection::MetadataInit("Rule", "benchmark.Rule",
                ::bond::reflection::Attributes()
            );
        }
    };
    

    //
    // Rules
    //
    struct Rules::Schema
    {
        typedef ::bond::no_base base;

        static const ::bond::Metadata metadata;
        
        private: static const ::bond::Metadata s_scopeCase_metadata;
        private: static const ::bond::Metadata s_subjectCase_metadata;

        public: struct var
        {
            // scopeCase
            typedef struct scopeCase_type : ::bond::reflection::FieldTemplate<
                0,
                ::bond::reflection::required_field_modifier,
                Rules,
                std::list< ::benchmark::Rule>,
                &Rules::scopeCase,
                &s_scopeCase_metadata
            > {} scopeCase;
        
            // subjectCase
            typedef struct subjectCase_type : ::bond::reflection::FieldTemplate<
                1,
                ::bond::reflection::required_field_modifier,
                Rules,
                std::list< ::benchmark::Rule>,
                &Rules::subjectCase,
                &s_subjectCase_metadata
            > {} subjectCase;
        };

        private: typedef boost::mpl::list<> fields0;
        private: typedef boost::mpl::push_front<fields0, var::subjectCase>::type fields1;
        private: typedef boost::mpl::push_front<fields1, var::scopeCase>::type fields2;

        public: typedef fields2::type fields;
        
        
        static ::bond::Metadata GetMetadata()
        {
            return ::bond::reflection::MetadataInit("Rules", "benchmark.Rules",
                ::bond::reflection::Attributes()
            );
        }
    };
    

    //
    // Main
    //
    struct Main::Schema
    {
        typedef ::bond::no_base base;

        static const ::bond::Metadata metadata;
        
        private: static const ::bond::Metadata s_rules_metadata;

        public: struct var
        {
            // rules
            typedef struct rules_type : ::bond::reflection::FieldTemplate<
                0,
                ::bond::reflection::required_field_modifier,
                Main,
                ::benchmark::Rules,
                &Main::rules,
                &s_rules_metadata
            > {} rules;
        };

        private: typedef boost::mpl::list<> fields0;
        private: typedef boost::mpl::push_front<fields0, var::rules>::type fields1;

        public: typedef fields1::type fields;
        
        
        static ::bond::Metadata GetMetadata()
        {
            return ::bond::reflection::MetadataInit("Main", "benchmark.Main",
                ::bond::reflection::Attributes()
            );
        }
    };
    

    
} // namespace benchmark
