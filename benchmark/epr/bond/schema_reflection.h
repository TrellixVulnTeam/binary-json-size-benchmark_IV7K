
//------------------------------------------------------------------------------
// This code was generated by a tool.
//
//   Tool : Bond Compiler 0.12.1.0
//   Input filename:  benchmark/epr/bond/schema.bond
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
        
        private: static const ::bond::Metadata s_path_metadata;
        private: static const ::bond::Metadata s_regex_metadata;
        private: static const ::bond::Metadata s_types_metadata;
        private: static const ::bond::Metadata s_allowData_metadata;

        public: struct var
        {
            // path
            typedef struct path_type : ::bond::reflection::FieldTemplate<
                0,
                ::bond::reflection::optional_field_modifier,
                Rule,
                std::string,
                &Rule::path,
                &s_path_metadata
            > {} path;
        
            // regex
            typedef struct regex_type : ::bond::reflection::FieldTemplate<
                1,
                ::bond::reflection::optional_field_modifier,
                Rule,
                std::string,
                &Rule::regex,
                &s_regex_metadata
            > {} regex;
        
            // types
            typedef struct types_type : ::bond::reflection::FieldTemplate<
                2,
                ::bond::reflection::required_field_modifier,
                Rule,
                std::list<std::string>,
                &Rule::types,
                &s_types_metadata
            > {} types;
        
            // allowData
            typedef struct allowData_type : ::bond::reflection::FieldTemplate<
                3,
                ::bond::reflection::required_field_modifier,
                Rule,
                bool,
                &Rule::allowData,
                &s_allowData_metadata
            > {} allowData;
        };

        private: typedef boost::mpl::list<> fields0;
        private: typedef boost::mpl::push_front<fields0, var::allowData>::type fields1;
        private: typedef boost::mpl::push_front<fields1, var::types>::type fields2;
        private: typedef boost::mpl::push_front<fields2, var::regex>::type fields3;
        private: typedef boost::mpl::push_front<fields3, var::path>::type fields4;

        public: typedef fields4::type fields;
        
        
        static ::bond::Metadata GetMetadata()
        {
            return ::bond::reflection::MetadataInit("Rule", "benchmark.Rule",
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
        
        private: static const ::bond::Metadata s_site_metadata;
        private: static const ::bond::Metadata s_maxAge_metadata;
        private: static const ::bond::Metadata s_reportUrl_metadata;
        private: static const ::bond::Metadata s_defaultNavBehavior_metadata;
        private: static const ::bond::Metadata s_defaultResBehavior_metadata;
        private: static const ::bond::Metadata s_rules_metadata;

        public: struct var
        {
            // site
            typedef struct site_type : ::bond::reflection::FieldTemplate<
                0,
                ::bond::reflection::required_field_modifier,
                Main,
                std::string,
                &Main::site,
                &s_site_metadata
            > {} site;
        
            // maxAge
            typedef struct maxAge_type : ::bond::reflection::FieldTemplate<
                1,
                ::bond::reflection::required_field_modifier,
                Main,
                uint32_t,
                &Main::maxAge,
                &s_maxAge_metadata
            > {} maxAge;
        
            // reportUrl
            typedef struct reportUrl_type : ::bond::reflection::FieldTemplate<
                2,
                ::bond::reflection::required_field_modifier,
                Main,
                std::string,
                &Main::reportUrl,
                &s_reportUrl_metadata
            > {} reportUrl;
        
            // defaultNavBehavior
            typedef struct defaultNavBehavior_type : ::bond::reflection::FieldTemplate<
                3,
                ::bond::reflection::required_field_modifier,
                Main,
                std::string,
                &Main::defaultNavBehavior,
                &s_defaultNavBehavior_metadata
            > {} defaultNavBehavior;
        
            // defaultResBehavior
            typedef struct defaultResBehavior_type : ::bond::reflection::FieldTemplate<
                4,
                ::bond::reflection::required_field_modifier,
                Main,
                std::string,
                &Main::defaultResBehavior,
                &s_defaultResBehavior_metadata
            > {} defaultResBehavior;
        
            // rules
            typedef struct rules_type : ::bond::reflection::FieldTemplate<
                5,
                ::bond::reflection::required_field_modifier,
                Main,
                std::list< ::benchmark::Rule>,
                &Main::rules,
                &s_rules_metadata
            > {} rules;
        };

        private: typedef boost::mpl::list<> fields0;
        private: typedef boost::mpl::push_front<fields0, var::rules>::type fields1;
        private: typedef boost::mpl::push_front<fields1, var::defaultResBehavior>::type fields2;
        private: typedef boost::mpl::push_front<fields2, var::defaultNavBehavior>::type fields3;
        private: typedef boost::mpl::push_front<fields3, var::reportUrl>::type fields4;
        private: typedef boost::mpl::push_front<fields4, var::maxAge>::type fields5;
        private: typedef boost::mpl::push_front<fields5, var::site>::type fields6;

        public: typedef fields6::type fields;
        
        
        static ::bond::Metadata GetMetadata()
        {
            return ::bond::reflection::MetadataInit("Main", "benchmark.Main",
                ::bond::reflection::Attributes()
            );
        }
    };
    

    
} // namespace benchmark
