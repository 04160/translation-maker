<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

    public function test(Request $request)
    {
        $array_var = [
            'key_one' => 'value_one',
            'key_two' => 'value_two'
        ];
        $var_three = "value_three"; #another comment
        $var_four = 'value_four'; //comment
        $translation_arr = [ __('translation.first_one'), trans('translation.second_one') ];
        $multiline_translation = trans(
            'translation.multiline1'
        );
        $multiline_translation2 = trans(
            'translation.' .
            'multiline2'
        );
        $translations = [
            __('translation.simpletext'),
            __("translation.$var_three"),
            __('translation.' . $var_four),
            __('translation.' . $array_var['key_one']),
            __('translation.' . $array_var["key_two"])
        ];
    }
}
