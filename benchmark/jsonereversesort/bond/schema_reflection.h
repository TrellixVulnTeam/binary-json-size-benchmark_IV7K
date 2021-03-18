
//------------------------------------------------------------------------------
// This code was generated by a tool.
//
//   Tool : Bond Compiler 0.12.1.0
//   Input filename:  benchmark/jsonereversesort/bond/schema.bond
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
    // Let
    //
    struct Let::Schema
    {
        typedef ::bond::no_base base;

        static const ::bond::Metadata metadata;
        
        private: static const ::bond::Metadata s_x_metadata;

        public: struct var
        {
            // x
            typedef struct x_type : ::bond::reflection::FieldTemplate<
                0,
                ::bond::reflection::required_field_modifier,
                Let,
                std::list<uint8_t>,
                &Let::x,
                &s_x_metadata
            > {} x;
        };

        private: typedef boost::mpl::list<> fields0;
        private: typedef boost::mpl::push_front<fields0, var::x>::type fields1;

        public: typedef fields1::type fields;
        
        
        static ::bond::Metadata GetMetadata()
        {
            return ::bond::reflection::MetadataInit("Let", "benchmark.Let",
                ::bond::reflection::Attributes()
            );
        }
    };
    

    //
    // Sort
    //
    struct Sort::Schema
    {
        typedef ::bond::no_base base;

        static const ::bond::Metadata metadata;
        
        private: static const ::bond::Metadata s_eval_metadata;

        public: struct var
        {
            // eval
            typedef struct eval_type : ::bond::reflection::FieldTemplate<
                0,
                ::bond::reflection::required_field_modifier,
                Sort,
                std::string,
                &Sort::eval,
                &s_eval_metadata
            > {} eval;
        };

        private: typedef boost::mpl::list<> fields0;
        private: typedef boost::mpl::push_front<fields0, var::eval>::type fields1;

        public: typedef fields1::type fields;
        
        
        static ::bond::Metadata GetMetadata()
        {
            return ::bond::reflection::MetadataInit("Sort", "benchmark.Sort",
                ::bond::reflection::Attributes()
            );
        }
    };
    

    //
    // Reverse
    //
    struct Reverse::Schema
    {
        typedef ::bond::no_base base;

        static const ::bond::Metadata metadata;
        
        private: static const ::bond::Metadata s_sort_metadata;
        private: static const ::bond::Metadata s_byX_metadata;

        public: struct var
        {
            // sort
            typedef struct sort_type : ::bond::reflection::FieldTemplate<
                0,
                ::bond::reflection::required_field_modifier,
                Reverse,
                ::benchmark::Sort,
                &Reverse::sort,
                &s_sort_metadata
            > {} sort;
        
            // byX
            typedef struct byX_type : ::bond::reflection::FieldTemplate<
                1,
                ::bond::reflection::required_field_modifier,
                Reverse,
                std::string,
                &Reverse::byX,
                &s_byX_metadata
            > {} byX;
        };

        private: typedef boost::mpl::list<> fields0;
        private: typedef boost::mpl::push_front<fields0, var::byX>::type fields1;
        private: typedef boost::mpl::push_front<fields1, var::sort>::type fields2;

        public: typedef fields2::type fields;
        
        
        static ::bond::Metadata GetMetadata()
        {
            return ::bond::reflection::MetadataInit("Reverse", "benchmark.Reverse",
                ::bond::reflection::Attributes()
            );
        }
    };
    

    //
    // In
    //
    struct In::Schema
    {
        typedef ::bond::no_base base;

        static const ::bond::Metadata metadata;
        
        private: static const ::bond::Metadata s_reverse_metadata;

        public: struct var
        {
            // reverse
            typedef struct reverse_type : ::bond::reflection::FieldTemplate<
                0,
                ::bond::reflection::required_field_modifier,
                In,
                ::benchmark::Reverse,
                &In::reverse,
                &s_reverse_metadata
            > {} reverse;
        };

        private: typedef boost::mpl::list<> fields0;
        private: typedef boost::mpl::push_front<fields0, var::reverse>::type fields1;

        public: typedef fields1::type fields;
        
        
        static ::bond::Metadata GetMetadata()
        {
            return ::bond::reflection::MetadataInit("In", "benchmark.In",
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
        
        private: static const ::bond::Metadata s_let_metadata;
        private: static const ::bond::Metadata s_in_metadata;

        public: struct var
        {
            // let
            typedef struct let_type : ::bond::reflection::FieldTemplate<
                0,
                ::bond::reflection::required_field_modifier,
                Main,
                ::benchmark::Let,
                &Main::let,
                &s_let_metadata
            > {} let;
        
            // in
            typedef struct in_type : ::bond::reflection::FieldTemplate<
                1,
                ::bond::reflection::required_field_modifier,
                Main,
                ::benchmark::In,
                &Main::in,
                &s_in_metadata
            > {} in;
        };

        private: typedef boost::mpl::list<> fields0;
        private: typedef boost::mpl::push_front<fields0, var::in>::type fields1;
        private: typedef boost::mpl::push_front<fields1, var::let>::type fields2;

        public: typedef fields2::type fields;
        
        
        static ::bond::Metadata GetMetadata()
        {
            return ::bond::reflection::MetadataInit("Main", "benchmark.Main",
                ::bond::reflection::Attributes()
            );
        }
    };
    

    
} // namespace benchmark