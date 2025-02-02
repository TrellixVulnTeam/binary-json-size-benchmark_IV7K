
//------------------------------------------------------------------------------
// This code was generated by a tool.
//
//   Tool : Bond Compiler 0.12.1.0
//   Input filename:  benchmark/packagejson/bond/schema.bond
//   Output filename: schema_types.h
//
// Changes to this file may cause incorrect behavior and will be lost when
// the code is regenerated.
// <auto-generated />
//------------------------------------------------------------------------------

#pragma once

#include <bond/core/bond_version.h>

#if BOND_VERSION < 0x0902
#error This file was generated by a newer version of the Bond compiler and is incompatible with your version of the Bond library.
#endif

#if BOND_MIN_CODEGEN_VERSION > 0x0c10
#error This file was generated by an older version of the Bond compiler and is incompatible with your version of the Bond library.
#endif

#include <bond/core/config.h>
#include <bond/core/containers.h>



namespace benchmark
{
    
    struct Author
    {
        std::string name;
        std::string url;
        
        Author()
        {
        }

        
        // Compiler generated copy ctor OK
        Author(const Author&) = default;
        
        Author(Author&&) = default;
        
        
        // Compiler generated operator= OK
        Author& operator=(const Author&) = default;
        Author& operator=(Author&&) = default;

        bool operator==(const Author& other) const
        {
            return true
                && (name == other.name)
                && (url == other.url);
        }

        bool operator!=(const Author& other) const
        {
            return !(*this == other);
        }

        void swap(Author& other)
        {
            using std::swap;
            swap(name, other.name);
            swap(url, other.url);
        }

        struct Schema;

    protected:
        void InitMetadata(const char*, const char*)
        {
        }
    };

    inline void swap(::benchmark::Author& left, ::benchmark::Author& right)
    {
        left.swap(right);
    }

    
    struct Repository
    {
        std::string type;
        std::string url;
        
        Repository()
        {
        }

        
        // Compiler generated copy ctor OK
        Repository(const Repository&) = default;
        
        Repository(Repository&&) = default;
        
        
        // Compiler generated operator= OK
        Repository& operator=(const Repository&) = default;
        Repository& operator=(Repository&&) = default;

        bool operator==(const Repository& other) const
        {
            return true
                && (type == other.type)
                && (url == other.url);
        }

        bool operator!=(const Repository& other) const
        {
            return !(*this == other);
        }

        void swap(Repository& other)
        {
            using std::swap;
            swap(type, other.type);
            swap(url, other.url);
        }

        struct Schema;

    protected:
        void InitMetadata(const char*, const char*)
        {
        }
    };

    inline void swap(::benchmark::Repository& left, ::benchmark::Repository& right)
    {
        left.swap(right);
    }

    
    struct Bugs
    {
        std::string url;
        
        Bugs()
        {
        }

        
        // Compiler generated copy ctor OK
        Bugs(const Bugs&) = default;
        
        Bugs(Bugs&&) = default;
        
        
        // Compiler generated operator= OK
        Bugs& operator=(const Bugs&) = default;
        Bugs& operator=(Bugs&&) = default;

        bool operator==(const Bugs& other) const
        {
            return true
                && (url == other.url);
        }

        bool operator!=(const Bugs& other) const
        {
            return !(*this == other);
        }

        void swap(Bugs& other)
        {
            using std::swap;
            swap(url, other.url);
        }

        struct Schema;

    protected:
        void InitMetadata(const char*, const char*)
        {
        }
    };

    inline void swap(::benchmark::Bugs& left, ::benchmark::Bugs& right)
    {
        left.swap(right);
    }

    
    struct License
    {
        std::string type;
        std::string url;
        
        License()
        {
        }

        
        // Compiler generated copy ctor OK
        License(const License&) = default;
        
        License(License&&) = default;
        
        
        // Compiler generated operator= OK
        License& operator=(const License&) = default;
        License& operator=(License&&) = default;

        bool operator==(const License& other) const
        {
            return true
                && (type == other.type)
                && (url == other.url);
        }

        bool operator!=(const License& other) const
        {
            return !(*this == other);
        }

        void swap(License& other)
        {
            using std::swap;
            swap(type, other.type);
            swap(url, other.url);
        }

        struct Schema;

    protected:
        void InitMetadata(const char*, const char*)
        {
        }
    };

    inline void swap(::benchmark::License& left, ::benchmark::License& right)
    {
        left.swap(right);
    }

    
    struct Scripts
    {
        std::string test;
        
        Scripts()
        {
        }

        
        // Compiler generated copy ctor OK
        Scripts(const Scripts&) = default;
        
        Scripts(Scripts&&) = default;
        
        
        // Compiler generated operator= OK
        Scripts& operator=(const Scripts&) = default;
        Scripts& operator=(Scripts&&) = default;

        bool operator==(const Scripts& other) const
        {
            return true
                && (test == other.test);
        }

        bool operator!=(const Scripts& other) const
        {
            return !(*this == other);
        }

        void swap(Scripts& other)
        {
            using std::swap;
            swap(test, other.test);
        }

        struct Schema;

    protected:
        void InitMetadata(const char*, const char*)
        {
        }
    };

    inline void swap(::benchmark::Scripts& left, ::benchmark::Scripts& right)
    {
        left.swap(right);
    }

    
    struct Engines
    {
        std::string node;
        
        Engines()
        {
        }

        
        // Compiler generated copy ctor OK
        Engines(const Engines&) = default;
        
        Engines(Engines&&) = default;
        
        
        // Compiler generated operator= OK
        Engines& operator=(const Engines&) = default;
        Engines& operator=(Engines&&) = default;

        bool operator==(const Engines& other) const
        {
            return true
                && (node == other.node);
        }

        bool operator!=(const Engines& other) const
        {
            return !(*this == other);
        }

        void swap(Engines& other)
        {
            using std::swap;
            swap(node, other.node);
        }

        struct Schema;

    protected:
        void InitMetadata(const char*, const char*)
        {
        }
    };

    inline void swap(::benchmark::Engines& left, ::benchmark::Engines& right)
    {
        left.swap(right);
    }

    
    struct Dependencies
    {
        std::string async;
        std::string coffeeScript;
        std::string colors;
        std::string dateformat;
        std::string eventemitter2;
        std::string findupSync;
        std::string glob;
        std::string hooker;
        std::string iconvLite;
        std::string minimatch;
        std::string nopt;
        std::string rimraf;
        std::string lodash;
        std::string underscoreString;
        std::string which;
        std::string jsYaml;
        std::string exit;
        std::string getobject;
        std::string gruntLegacyUtil;
        std::string gruntLegacyLog;
        
        Dependencies()
        {
        }

        
        // Compiler generated copy ctor OK
        Dependencies(const Dependencies&) = default;
        
        Dependencies(Dependencies&&) = default;
        
        
        // Compiler generated operator= OK
        Dependencies& operator=(const Dependencies&) = default;
        Dependencies& operator=(Dependencies&&) = default;

        bool operator==(const Dependencies& other) const
        {
            return true
                && (async == other.async)
                && (coffeeScript == other.coffeeScript)
                && (colors == other.colors)
                && (dateformat == other.dateformat)
                && (eventemitter2 == other.eventemitter2)
                && (findupSync == other.findupSync)
                && (glob == other.glob)
                && (hooker == other.hooker)
                && (iconvLite == other.iconvLite)
                && (minimatch == other.minimatch)
                && (nopt == other.nopt)
                && (rimraf == other.rimraf)
                && (lodash == other.lodash)
                && (underscoreString == other.underscoreString)
                && (which == other.which)
                && (jsYaml == other.jsYaml)
                && (exit == other.exit)
                && (getobject == other.getobject)
                && (gruntLegacyUtil == other.gruntLegacyUtil)
                && (gruntLegacyLog == other.gruntLegacyLog);
        }

        bool operator!=(const Dependencies& other) const
        {
            return !(*this == other);
        }

        void swap(Dependencies& other)
        {
            using std::swap;
            swap(async, other.async);
            swap(coffeeScript, other.coffeeScript);
            swap(colors, other.colors);
            swap(dateformat, other.dateformat);
            swap(eventemitter2, other.eventemitter2);
            swap(findupSync, other.findupSync);
            swap(glob, other.glob);
            swap(hooker, other.hooker);
            swap(iconvLite, other.iconvLite);
            swap(minimatch, other.minimatch);
            swap(nopt, other.nopt);
            swap(rimraf, other.rimraf);
            swap(lodash, other.lodash);
            swap(underscoreString, other.underscoreString);
            swap(which, other.which);
            swap(jsYaml, other.jsYaml);
            swap(exit, other.exit);
            swap(getobject, other.getobject);
            swap(gruntLegacyUtil, other.gruntLegacyUtil);
            swap(gruntLegacyLog, other.gruntLegacyLog);
        }

        struct Schema;

    protected:
        void InitMetadata(const char*, const char*)
        {
        }
    };

    inline void swap(::benchmark::Dependencies& left, ::benchmark::Dependencies& right)
    {
        left.swap(right);
    }

    
    struct DevDependencies
    {
        std::string temporary;
        std::string gruntContribJshint;
        std::string gruntContribNodeunit;
        std::string gruntContribWatch;
        std::string difflet;
        std::string semver;
        std::string shelljs;
        
        DevDependencies()
        {
        }

        
        // Compiler generated copy ctor OK
        DevDependencies(const DevDependencies&) = default;
        
        DevDependencies(DevDependencies&&) = default;
        
        
        // Compiler generated operator= OK
        DevDependencies& operator=(const DevDependencies&) = default;
        DevDependencies& operator=(DevDependencies&&) = default;

        bool operator==(const DevDependencies& other) const
        {
            return true
                && (temporary == other.temporary)
                && (gruntContribJshint == other.gruntContribJshint)
                && (gruntContribNodeunit == other.gruntContribNodeunit)
                && (gruntContribWatch == other.gruntContribWatch)
                && (difflet == other.difflet)
                && (semver == other.semver)
                && (shelljs == other.shelljs);
        }

        bool operator!=(const DevDependencies& other) const
        {
            return !(*this == other);
        }

        void swap(DevDependencies& other)
        {
            using std::swap;
            swap(temporary, other.temporary);
            swap(gruntContribJshint, other.gruntContribJshint);
            swap(gruntContribNodeunit, other.gruntContribNodeunit);
            swap(gruntContribWatch, other.gruntContribWatch);
            swap(difflet, other.difflet);
            swap(semver, other.semver);
            swap(shelljs, other.shelljs);
        }

        struct Schema;

    protected:
        void InitMetadata(const char*, const char*)
        {
        }
    };

    inline void swap(::benchmark::DevDependencies& left, ::benchmark::DevDependencies& right)
    {
        left.swap(right);
    }

    
    struct Main
    {
        std::string name;
        std::string description;
        std::string version;
        ::benchmark::Author author;
        std::string homepage;
        ::benchmark::Repository repository;
        ::benchmark::Bugs bugs;
        std::list< ::benchmark::License> licenses;
        std::string main;
        ::benchmark::Scripts scripts;
        ::benchmark::Engines engines;
        std::list<std::string> keywords;
        ::benchmark::Dependencies dependencies;
        ::benchmark::DevDependencies devDependencies;
        std::string readme;
        std::string _id;
        std::string _from;
        
        Main()
        {
        }

        
        // Compiler generated copy ctor OK
        Main(const Main&) = default;
        
        Main(Main&&) = default;
        
        
        // Compiler generated operator= OK
        Main& operator=(const Main&) = default;
        Main& operator=(Main&&) = default;

        bool operator==(const Main& other) const
        {
            return true
                && (name == other.name)
                && (description == other.description)
                && (version == other.version)
                && (author == other.author)
                && (homepage == other.homepage)
                && (repository == other.repository)
                && (bugs == other.bugs)
                && (licenses == other.licenses)
                && (main == other.main)
                && (scripts == other.scripts)
                && (engines == other.engines)
                && (keywords == other.keywords)
                && (dependencies == other.dependencies)
                && (devDependencies == other.devDependencies)
                && (readme == other.readme)
                && (_id == other._id)
                && (_from == other._from);
        }

        bool operator!=(const Main& other) const
        {
            return !(*this == other);
        }

        void swap(Main& other)
        {
            using std::swap;
            swap(name, other.name);
            swap(description, other.description);
            swap(version, other.version);
            swap(author, other.author);
            swap(homepage, other.homepage);
            swap(repository, other.repository);
            swap(bugs, other.bugs);
            swap(licenses, other.licenses);
            swap(main, other.main);
            swap(scripts, other.scripts);
            swap(engines, other.engines);
            swap(keywords, other.keywords);
            swap(dependencies, other.dependencies);
            swap(devDependencies, other.devDependencies);
            swap(readme, other.readme);
            swap(_id, other._id);
            swap(_from, other._from);
        }

        struct Schema;

    protected:
        void InitMetadata(const char*, const char*)
        {
        }
    };

    inline void swap(::benchmark::Main& left, ::benchmark::Main& right)
    {
        left.swap(right);
    }
} // namespace benchmark
