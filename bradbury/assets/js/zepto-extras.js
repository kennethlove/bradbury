(function($) {
  // Used by bootstrap
  $.support = {};

  // Used by bootstrap
  $.proxy = function( fn, context ) {
    if ( typeof context === "string" ) {
      var tmp = fn[ context ];
      context = fn;
      fn = tmp;
    }

    // Quick check to determine if target is callable, in the spec
    // this throws a TypeError, but we will just return undefined.
    if ( !$.isFunction( fn ) ) {
      return undefined;
    }

    // Simulated bind
    var args = Array.prototype.slice.call( arguments, 2 ),
      proxy = function() {
        return fn.apply( context, args.concat( Array.prototype.slice.call( arguments ) ) );
      };

    // Set the guid of unique handler to the same of original handler, so it can be removed
    proxy.guid = fn.guid = fn.guid || proxy.guid || $.guid++;

    return proxy;
  };
})(Zepto);
